import tensorflow as tf
import numpy as np

once_size = 50   # 输入层的数据一次输入多少，不要过大
seed = 22       # 随便设个固定值，保证每次生成的都一样
step = 0.001    # 每次优化loss调整的步长
counts = 400    # 训练次数
boys = 45       # 45条数据

rng = np.random.RandomState(seed)  # 用这个rng生成每次都一样的随机数（seed相同）
X = rng.rand(boys, 2)  # 随机生成一个班级45个学生的颜值和财富（特征值范围[0, 1)),有现成数据更好

# 我们定义颜值+财富小于1的对应的Y值结果为0（假定0就是找不到女朋友），否则为1（能找到女朋友）
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

# # 定义男孩的输入特征（颜值和财富）和权重
x_data = tf.placeholder(tf.float32, shape=(None, 2))    #
y_data = tf.placeholder(tf.float32, shape=(None, 1))    # 最终输出的结果
#
w1 = tf.Variable(tf.random_normal([2, 30], stddev=1, seed=None))
w2 = tf.Variable(tf.random_normal([30, 1], stddev=1, seed=None))
#
a = tf.matmul(x_data, w1)
y = tf.matmul(a, w2)
#
# 定义损失函数及反向传播方法
loss = tf.reduce_mean(tf.square(y - y_data))          # 均方误差
train_step = tf.train.GradientDescentOptimizer(step).minimize(loss)  # 梯度下降法优化loss

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for count in range(counts):  # 训练counts次
        start = (count * once_size) % boys  # 0  5   10
        end = start + once_size             # 5  10  15
        # 一次训练（前向传播和反向传播）5组数据
        sess.run(train_step, feed_dict={x_data: X[start:end], y_data: Y[start:end]})
        if count % 200 == 0:     # 每训练200次输出优化后的损失值
            now_loss = sess.run(loss, feed_dict={x_data: X, y_data: Y})
            print(now_loss)
