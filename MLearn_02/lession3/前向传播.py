import tensorflow as tf
import time
'''
seed为随机种子，随机种子值一样，生成的随机数一样
stddev标准差（超过这个标准差，数据重新生成）
mean方差
'''

# w = tf.Variable(tf.random_normal([2, 3], stddev=2, mean=0, seed=1))
# w2 = tf.Variable(tf.random_normal([2, 3], stddev=2, mean=0, seed=2))
# w3 = tf.Variable(tf.random_normal([2, 3], stddev=2, mean=0, seed=1))
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)
# print(sess.run(w))
# print(sess.run(w2))
# print(sess.run(w3))

# 每个男生的财富x1[0, 1)  0.7
# 每个男生的颜值x2[0, 1)  0.4

# # x1   x2     y
#   0.1  0.4    0
#   0.8  0.3    1

'''
案例：
我们采集一部分男生的颜值x1和财富x2作为特征输入NN，通过NN后输出一个数值
x_data作为输入层我们先用一个男生的数据（一个1行2列的矩阵）
w(1)我们作为第一层输入的权重构建一个（2行N列的矩阵，先假定N=3）
a(1)就是通过x_data和w(1)的叉乘得出的第一层神经网络
（我们说的神经网络有几层是指有多少计算层，当前神经网络是第几层是指第几个计算层）

'''

# 定义一个男孩的特征,构建一个两次神经网络
# import tensorflow as tf
#
# # 定义一个男孩的输入特征（颜值和财富）和权重
# x_data = tf.constant([[0.4, 0.8]])   # 一个同学的颜值和财富(shape(1, 2))

# 如果我想随机生成N个1行2列的矩阵（每个元素范围在[0, 1)]
#[[x1, x2]
 #[x1, x2]]
# w1 = tf.Variable(tf.random_normal([2, 3], stddev=2, seed=1))  # [0.4, 0.5, 0.2], [0.3, 0.7, 0.2]
# w2 = tf.Variable(tf.random_normal([3, 1], stddev=2, seed=1))  # [0.2], [0.5], [0.21]
# #
# # # 定义前向传播过程
# a = tf.matmul(x_data, w1)   # x_data： 1行2列； w1：2行3列
# y = tf.matmul(a, w2)        # 1行1列
#
# # 进入会话计算结果
# with tf.Session() as sess:
#     init = tf.global_variables_initializer()
#     sess.run(init)
#     y = sess.run(y)
#     print(y)

#////////////////////////////////////////////////////////////////
# 定义多个男孩的特征，构建一个两层神经网络
# import tensorflow as tf
#
# 定义N个男孩的输入特征（颜值和财富）和权重
# x_data = tf.placeholder(tf.float32, shape=(None, 2))  # n 2
#
# w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))  # 2 3
# w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))  # n 1
#
# # 定义前向传播过程
# a = tf.matmul(x_data, w1)
# y = tf.matmul(a, w2)
#
# # 进入会话计算结果
# boyes = [[0.1, 0.01], [0.9, 0.98], [0.2, 0.97], [0.9, 0.1]]
# with tf.Session() as sess:
#     init = tf.global_variables_initializer()
#     sess.run(init)
#     y = sess.run(y, feed_dict={x_data: boyes})
#     print(y)
