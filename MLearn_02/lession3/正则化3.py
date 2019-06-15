# coding:utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

one_size = 50
seed = 2
counts = 50000    # 训练次数
step = 0.1    # 每次优化loss调整的步长
datas_count = 500

rdm = np.random.RandomState(seed)
X = rdm.randn(datas_count, 2)  # 生成500行2列的矩阵(x1,x2)
Y = [int(x1 * x1 + x2 * x2 < 2) for (x1, x2) in X]
Y_COLOR = [['RED' if y else 'BLUE'] for y in Y]
#print(Y_COLOR)

# vstack(Y)把list转为numpy数据类型,reshape(-1, 1)保留原来结构转为1列

Y = np.vstack(Y).reshape(-1, 1)

def get_weight(shape, regularizer):  # 对w进行正则化
    w = tf.Variable(tf.random_normal(shape))
    # l2_regularizer表示对sum(w^2)
    tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w

def get_bias(shape):
    b = tf.Variable(tf.constant(0.01, shape=shape))
    return b

x_data = tf.placeholder(tf.float32, shape=(None, 2))
y_data = tf.placeholder(tf.float32, shape=(None, 1))

w1 = get_weight([2, 11], 0.01)
b1 = get_bias([11])
y1 = tf.nn.relu(tf.matmul(x_data, w1) + b1)  # 激活函数
w2 = get_weight([11, 1], 0.01)
b2 = get_bias([1])

y = tf.matmul(y1, w2) + b2

# 定义损失函数
loss = tf.reduce_mean(tf.square(y - y_data))
loss_total = loss + tf.add_n(tf.get_collection("losses"))

# 反向传播(正则化)
train_step = tf.train.AdadeltaOptimizer(step).minimize(loss_total)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for count in range(counts):
        start = (count * one_size) % datas_count
        end = start + one_size
        sess.run(train_step, feed_dict={x_data: X[start: end], y_data: Y[start: end]})
        if count % 2000 == 0:
            loss_now = sess.run(loss, feed_dict={x_data: X, y_data: Y})
            print("第%s轮训练后的loss值：%s" % (count, loss_now))
    xx, yy = np.mgrid[-3: 3: 0.01, -3: 3: 0.01]
    grid = np.c_[xx.ravel(), yy.ravel()]
    probs = sess.run(y, feed_dict={x_data: grid})

    probs = probs.reshape(xx.shape)

    print("w1:\n", sess.run(w1))
    print("b1:\n", sess.run(b1))
    print("w2:\n", sess.run(w2))
    print("b2:\n", sess.run(b2))

plt.scatter(X[:, 0], X[:, 1], c=np.squeeze(Y_COLOR))
plt.contour(xx, yy, probs, levels=[0.5])
plt.show()



