# coding:utf-8
import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import generateds
import forward


ONE_SIZE = 25   # 一次喂入神经网络25条数据
STEPS = 50000   # 运算的次数（每次给ONE_SIZE跳数据）

LEARNING_RATE_BASE = 0.09   # 学习率
LEARNING_RATE_DECAY = 0.99

REGULARIZER = 0.01  # 正则化

DATAS_COUNT = 500   # 共500条数据（样本特征值）

def backward():
    x_data = tf.placeholder(tf.float32, shape=(None, 2))
    y_data = tf.placeholder(tf.float32, shape=(None, 1))

    X, Y, Y_COLOR = generateds.generateds()
    y = forward.forward(x_data, REGULARIZER)

    global_step = tf.Variable(0, trainable=False)
    learning_rate = tf.train.exponential_decay(
    LEARNING_RATE_BASE,
    global_step,
    DATAS_COUNT/ONE_SIZE,
    LEARNING_RATE_BASE,
    staircase=True)

    loss = tf.reduce_mean(tf.square(y - y_data))
    loss_total = loss + tf.add_n(tf.get_collection("losses"))

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss_total)

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        for count in range(STEPS):
            start = (count * ONE_SIZE) % DATAS_COUNT
            end = start + ONE_SIZE
            sess.run(train_step, feed_dict={x_data: X[start: end], y_data: Y[start: end]})

            if count % 2000 == 0:
                loss_now = sess.run(loss_total, feed_dict={x_data: X, y_data: Y})
                print("第%s轮训练的loss值为%s" %(count, loss_now))
        xx, yy = np.mgrid[-3: 3: 0.01, -3: 3: 0.01]
        grid = np.c_[xx.ravel(), yy.ravel()]
        probs = sess.run(y, feed_dict={x_data: grid})

        probs = probs.reshape(xx.shape)  # 整理成和xx一样的shape

    plt.scatter(X[:, 0], X[:, 1], c=np.squeeze(Y_COLOR))
    plt.contour(xx, yy, probs, levels=[0.5])
    plt.show()
if __name__ == "__main__":
    backward()