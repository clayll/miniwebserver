# coding:utf-8
'''
设损失函数 loss=(w+1)^2，令w初始值为20，通过反向传播求
最优解w（也就是求使loss最小对应的w值），使用指数衰减的
学习率，在迭代初期得到较高的下降速度，可以在较小的训练
轮数下取得收敛率
'''

# 代码示例

import tensorflow as tf
counts = 50  # 训练50轮
once_size = 8

learning_rate_base = 0.6   # 最初学习率
learning_rate_decay = 0.99  # 学习率衰减率
learning_rate_step = 1  # 喂入1轮once_size后，更新一次学习率，一般设为总样本数/once_size

global_step = tf.Variable(0, trainable=False)  # 计数器（第几个once_size,初始值False（不训练）)

# 定义指数下降学习率
learning_rate = tf.train.exponential_decay(learning_rate_base, global_step, learning_rate_step, learning_rate_decay, staircase=True)

w = tf.Variable(tf.constant(13.0))  # w初始化为3

loss = tf.square(w + 1)  # 损失函数loss
# 反向传播方法
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for count in range(1, counts + 1):
        sess.run(train_step)
        now_learning_rate = sess.run(learning_rate)
        now_global_step = sess.run(global_step)
        now_w = sess.run(w)
        now_loss = sess.run(loss)
        print("第%s次now_w:%s, now_learning_rate:%s, now_loss:%s" % (count, now_w, now_learning_rate, now_loss))
