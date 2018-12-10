import csv
import tensorflow as tf
import operator
from py.CNN import CNN
import numpy as np
import os


def generate_data():
    ll_train = []
    error_train = []
    tmp = []
    for file in os.listdir('../cpp_bc'):
        with open('../cpp_bc/' + file, 'rb') as f:
            tmp.append(f.readlines())
    print(len(ll_train))
    for file in os.listdir('../dataset'):
        error_train.append(get_top5(file))
    print(error_train)
    ll_train = tmp[0: 5]
    return ll_train, error_train


def get_top5(csv_name):
    reader = csv.reader(open('/root/tmp/dataset/' + csv_name), delimiter=',')
    data_list = dict(reader)
    for k, v in data_list.items():
        data_list[k] = float(v)
    sorted_list = sorted(data_list.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_list[:5]


def list_top5():
    error_list = []
    for f in os.listdir('/root/tmp/dataset/'):
        if f.split('.')[-1] == 'csv':
           # print(get_top5(f))
            error_list.append(get_top5(f))
    return error_list


def run_training():
    cnn = CNN()
    model = cnn.build_model()

    ll, error = generate_data()

    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    saver = tf.train.Saver()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    try:
        for step in np.arange(1000):
            print(step)
            if coord.should_stop():
                break
            _, train_acc, train_loss = sess.run([ll, error])
            print("loss:{} accuracy:{}".format(train_loss, train_acc))

    except tf.errors.OutOfRangeError:
        print("Done!!!")
    finally:
        coord.request_stop()
    coord.join(threads)
    sess.close()




