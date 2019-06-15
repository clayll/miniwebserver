import tensorflow as tf
import numpy as np

'''
产品销量问题
假定有两个因素（x1， x2）是影响产品销量的因素
'''

once_size = 5   # 输入层的数据一次输入多少，不要过大  
seed = 2233     # 随便设个固定值，保证每次生成的都一样
step = 0.001    # 每次优化loss调整的步长
counts = 1000  # 训练轮数
products = 45
noise = 0.05    # 自定义随机噪声在（-0.05到0.05之间）
rdm = np.random.RandomState(seed)  # 用这个rdm生成每次都一样的随机数（seed相同）
X = rdm.rand(products, 2)  # 随机生成45个影响产品销量的特征因子x1和x2（特征值范围[0, 1)),有现成数据更好
# 自己生成结果集（给一定的噪音）
Y = [[x1 + x2 + rdm.rand()/10.0 - noise] for (x1, x2) in X]


# 定义神经网络输入和输出形状
x_data = tf.placeholder(tf.float32, shape=(None, 2))
y_data = tf.placeholder(tf.float32, shape=(None, 1))

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))  # 定义一层神经网络（计算层一层）
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
a = tf.matmul(x_data, w1)
y = tf.matmul(a, w2)  # 结果

# 定义损失函数及反向传播方法
loss = tf.reduce_mean(tf.square(y - y_data))          # 均方误差
train_step = tf.train.GradientDescentOptimizer(step).minimize(loss)  # 梯度下降法优化loss

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for count in range(counts):  # 训练counts次
        start = (count * once_size) % products
        end = start + once_size
        # 一次训练（前向传播和反向传播）5组数据
        sess.run(train_step, feed_dict={x_data: X[start:end], y_data: Y[start:end]})
        if count % 100 == 0:      # 每训练500次输出优化后的w1的值

            now_loss = sess.run(loss, feed_dict={x_data: X, y_data: Y})
            print("count:{0}  nowLoss:{1}  w1:{2}  w2:{3}".format(count,now_loss,sess.run(w1),sess.run(w2)))
