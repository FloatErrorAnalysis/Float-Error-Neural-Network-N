import tensorflow as tf
import tensorflow.contrib.rnn as rnn
from py.util.data_generator import generate_ll, generate_error
import numpy as np


TIME_STEPS = 10
BATCH_SIZE = 10
HIDDEN_UNITS = 10
HIDDEN_UNITS1 = 30
LEARNING_RATE = 0.01
EPOCH = 10

TEST_EXAMPLES = 30


TRAIN_EXAMPLES = 30



def generate_data():
    tmp_2 = generate_ll()
    lst1 = []
    for i in tmp_2:
        lst2 = []
        for j in i:
            if len(j) != 0:
                lst2.append(ord(j))
        lst1.append(lst2)
    return np.array(lst1), np.array(generate_error())


X_train = generate_data()[0]
y_train = generate_data()[1]
X_train = np.reshape(X_train, newshape=(X_train.shape[0], 1, X_train.shape[1]))
y_train = np.reshape(y_train, newshape=(y_train.shape[0], 1, y_train.shape[1] * 2))
print(X_train.shape)
print("Y_TRAIN: ", y_train.shape)
print("X_TRAIN: ", X_train.shape)
print(len(X_train))
# define graph
graph = tf.Graph()
with graph.as_default():
    X_p = tf.placeholder(dtype=tf.float32, shape=(10, 1, 1411))
    y_p = tf.placeholder(dtype=tf.float32, shape=(10, 1, 10))

    print("XP: ", X_p.shape)
    print("YP: ", y_p.shape)

    lstm_forward_1 = rnn.BasicLSTMCell(num_units=HIDDEN_UNITS1)
    lstm_forward_2 = rnn.BasicLSTMCell(num_units=HIDDEN_UNITS)
    lstm_forward = rnn.MultiRNNCell(cells=[lstm_forward_1, lstm_forward_2])

    lstm_backward_1 = rnn.BasicLSTMCell(num_units=HIDDEN_UNITS1)
    lstm_backward_2 = rnn.BasicLSTMCell(num_units=HIDDEN_UNITS)
    lstm_backward = rnn.MultiRNNCell(cells=[lstm_backward_1, lstm_backward_2])

    outputs, states = tf.nn.bidirectional_dynamic_rnn(
        cell_fw=lstm_forward,
        cell_bw=lstm_backward,
        inputs=X_p,
        dtype=tf.float32
    )

    outputs_fw, outputs_bw = outputs[0], outputs[1]

    h = outputs_fw[:, :, :] + outputs_bw[:, :, :]

    cross_loss = tf.losses.softmax_cross_entropy(onehot_labels=y_p, logits=h)

    correct_prediction = tf.equal(tf.argmax(h, 1), tf.argmax(y_p, 1))

    accuracy = tf.reduce_mean(tf.cast(correct_prediction, dtype="float"))

    optimizer = tf.train.AdamOptimizer(LEARNING_RATE).minimize(loss=cross_loss)

with tf.Session(graph=graph) as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(1, EPOCH + 1):
        train_losses = []
        accus = []
        print('epoch: ', epoch)

        for j in range(TRAIN_EXAMPLES//BATCH_SIZE):
            _, train_loss, accu = sess.run(
                fetches=(optimizer, cross_loss, accuracy),
                feed_dict={
                    X_p: X_train[j * BATCH_SIZE: (j + 1) * BATCH_SIZE],
                    y_p: y_train[j * BATCH_SIZE: (j + 1) * BATCH_SIZE]
                }
            )
            train_losses.append(train_loss)
            accus.append(accu)
        print('Average training loss: ', sum(train_losses) / len(train_losses))
        print(accus)
        print('Accuracy: ', sum(accus) / len(accus))