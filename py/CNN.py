import tensorflow as tf


class CNN:
    def __init__(self):
        # 参数设置
        self.batch_size = 64
        # byte code的输入格式定义为 150 * 32
        self.input_x = 150
        self.input_y = 32
        self.output_size = 5
        # 正则项系数
        self.regular_scale = 0.001
        self.graph = tf.Graph()
        # 建立模型相关量
        self.x, self.y, self.keep_prob = self.build_placeholder()
        self.prediction = self.build_model()
        self.loss = self.build_loss()
        self.train_op = self.build_train_op()

    # 返回训练时需要传入的 placeholder 的值
    def build_placeholder(self):
        with self.graph.as_default():
            # 声明一个占位符，None表示输入的数量不定，input_x * input_y 输入的维度
            x = tf.placeholder(tf.float32, [None, self.input_x * self.input_y])
            # 输出定义
            y = tf.placeholder(tf.float32, [None, self.output_size])
            # dropout操作，减少过拟合，其实就是降低上一层某些输入的权重scale，甚至置为0，升高某些输入的权值，甚至置为2，防止评测曲线出现震荡，个人觉得样本较少时很必要
            # 使用占位符，由dropout自动确定scale，也可以自定义，比如0.5，根据tensorflow文档可知，程序中真实使用的值为1/0.5=2，也就是某些输入乘以2，同时某些输入乘以0
            keep_prob = tf.placeholder(tf.float32)

            return x, y, keep_prob

    # 建立这个模型
    # 返回值为之后的输出向量
    def build_model(self):
        with self.graph.as_default():
            # x_image又把x reshape成了input_x * input_y的形状，因为是bc，所以通道是1.作为训练时的input，-1代表数量不定
            x_image = tf.reshape(self.x, [-1, self.input_x, self.input_y, 1])

            # 第一层卷积操作 #
            # 第一二参数值得卷积核尺寸大小，即patch，第三个参数是图像通道数，第四个参数是卷积核的数目，代表会出现多少个卷积特征图像;
            w_conv1 = tf.Variable(tf.truncated_normal(shape=[5, 5, 1, 32], stddev=0.1),
                                  collections=[tf.GraphKeys.WEIGHTS, tf.GraphKeys.GLOBAL_VARIABLES])
            # 对于每一个卷积核都有一个对应的偏置量。
            b_conv1 = tf.Variable(tf.truncated_normal(shape=[32], stddev=0.1))
            # 卷积遍历各方向步数为1，SAME：边缘外自动补0，遍历相乘
            h_conv1 = tf.nn.relu(tf.nn.conv2d(x_image, w_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)
            h_pool1 = tf.nn.max_pool(h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

            # 第二层卷积操作 #
            # 32通道卷积，卷积出64个特征
            w_conv2 = tf.Variable(tf.truncated_normal(shape=[5, 5, 32, 64], stddev=0.1),
                                  collections=[tf.GraphKeys.WEIGHTS, tf.GraphKeys.GLOBAL_VARIABLES])
            # 64个偏执数据
            b_conv2 = tf.Variable(tf.truncated_normal(shape=[64], stddev=0.1))
            # 注意h_pool1是上一层的池化结果
            h_conv2 = tf.nn.relu(tf.nn.conv2d(h_pool1, w_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)
            h_pool2 = tf.nn.max_pool(h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

            # 第三层全连接操作 #
            # 二维张量，第一个参数3*32*64的patch，也可以认为是只有一行3*32*64个数据的卷积，第二个参数代表卷积个数共1024个
            w_fc1 = tf.Variable(
                tf.truncated_normal(shape=[int(h_pool2.shape[1]) * int(h_pool2.shape[2]) * 64, 1024], stddev=0.1),
                collections=[tf.GraphKeys.WEIGHTS, tf.GraphKeys.GLOBAL_VARIABLES])
            # 1024个偏执数据
            b_fc1 = tf.Variable(tf.truncated_normal(shape=[1024], stddev=0.1))
            # 将第二层卷积池化结果reshape成只有一行3*32*64个数据# [n_samples, 7, 7, 64] ->> [n_samples, 7*7*64]
            h_pool2_flat = tf.reshape(h_pool2, [-1, int(h_pool2.shape[1]) * int(h_pool2.shape[2]) * 64])
            # 卷积操作，结果是1*1*1024，单行乘以单列等于1*1矩阵，matmul实现最基本的矩阵相乘，不同于tf.nn.conv2d的遍历相乘，自动认为是前行向量后列向量
            h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)

            # dropout操作，减少过拟合，其实就是降低上一层某些输入的权重scale，甚至置为0，升高某些输入的权值，甚至置为2，防止评测曲线出现震荡，个人觉得样本较少时很必要
            # 使用占位符，由dropout自动确定scale，也可以自定义，比如0.5，根据tensorflow文档可知，程序中真实使用的值为1/0.5=2，也就是某些输入乘以2，同时某些输入乘以0
            h_fc1_drop = tf.nn.dropout(h_fc1, self.keep_prob)  # 对卷积结果执行dropout操作

            # 第四层输出操作 ##
            # 二维张量，1*1024矩阵卷积，输出结果与 output_size 大小一致
            w_fc2 = tf.Variable(tf.truncated_normal(shape=[1024, self.output_size], stddev=0.1),
                                collections=[tf.GraphKeys.WEIGHTS, tf.GraphKeys.GLOBAL_VARIABLES])
            b_fc2 = tf.Variable(tf.truncated_normal(shape=[self.output_size], stddev=0.1))
            # 最后的分类，结果为batch_size * output_size
            prediction = tf.matmul(h_fc1_drop, w_fc2) + b_fc2

            return prediction

    # 建立预测的损失函数
    def build_loss(self):
        with self.graph.as_default():
            mse = tf.losses.mean_squared_error(self.y, self.prediction)
            reg_term = self.build_regular_term()
            loss = mse + reg_term
            return loss

    # 建立正则项
    def build_regular_term(self):
        with self.graph.as_default():
            regular = tf.contrib.layers.l2_regularizer(scale=self.regular_scale)
            reg_term = tf.contrib.layers.apply_regularization(regular)
            return reg_term

    # 建立训练张量
    def build_train_op(self):
        with self.graph.as_default():
            train_op = tf.train.AdamOptimizer(beta2=0.9999).minimize(self.loss)
            return train_op
