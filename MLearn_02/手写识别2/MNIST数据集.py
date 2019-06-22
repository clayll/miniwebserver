'''
MNIST数据集共有7万张图片
提供6万张 28*28像素点的0-9的手写数字图片和标签用于训练
提供1万张28*28像素点的0-9的手写数字图片和标签用于测试

每张图片784个像素点（28*28）组成长度为784的1维数组作为输入特征
例如：[0, 0, 0, 0.25, 0.37, 0.25, 0.37，0.22, 0.37，0, 0, 0.25,.....] shape=[[1，784]]1行784列矩阵
结果用10个概率表示0-9出现的概率
7表示：[0, 0, 0, 0, 0, 0, 0, 1, 0, 0] shape=[1, 10]（表示7出现的概率100%，其它数字出现的概率为0）
'''


from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

'''
one_hot=True这个参数.one_hot表示用非零即1的数组保存图片表示的数值
比如一个图片上面写的是1,那个保存的就是[0,1,0,0,0,0,0,0,0,0]
如果data目录下已有数据集则不下载，如果没有则下载
'''
mnist = input_data.read_data_sets('./data/', one_hot=True)

# print(mnist.train.num_examples)       # 训练集个数
# print(mnist.validation.num_examples)  # 验证集个数
#
# print(mnist.test.num_examples)        # 测试集个数

#print(mnist.train.labels)    # 训练集所有标签（矩阵）
#print(mnist.train.images)   # 训练集所有图片（矩阵）


# print(mnist.train.labels[0])  # 取出第一个标签（向量 10个元素）
# print(mnist.train.images[0])
# print(mnist.train.labels[1])
# print(mnist.train.labels[2])
# print(mnist.train.labels[3])
# print(mnist.train.labels[4])
# print(mnist.train.labels[5])
# print(mnist.train.labels[6])
# print(mnist.train.labels[7])
# print(mnist.train.labels[8])
# print(mnist.train.labels[9])
#
# print(mnist.train.images[0])  # 取出第一个图片（向量 784个元素）

# one_size = 100
# xx, yy = mnist.train.next_batch(one_size)
# print(xx.shape)  # (100, 784)
# print(yy.shape)  # (100, 10)

# 从集合中取出全部变量生成一个列表和下面的语句对应
# tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(regularizer)(w))
# tf.get_collection("losses")
#
# tf.add_n([1, 3, 6, -9]) 列表中元素相加
# with tf.Session() as sess:
#     print(sess.run(tf.add_n([1, 3, 6, -9])))
#
# x = tf.constant(4, dtype=tf.int32)
# y = tf.cast(x, dtype=tf.float32)  # 转换类型(必须是可转换的比如int和float)
#
# with tf.Session() as sess:
#     print(sess.run(x))
#     print(sess.run(y))

# tf.argmax(x_data, axis) # 返回最大值所在的索引号axis对应数据的维度减1
# x_data = [[1, 3, 2], [4, 3, 6], [1, 3, 2], [4, 6, 2]]  # 1, 2, 1, 1
# with tf.Session() as sess:
#     print(sess.run(tf.argmax(x_data, 1)))  # [1, 2, 1, 1]

# x_data = [1, 3, 2]
# with tf.Session() as sess:
#     print(sess.run(tf.argmax(x_data, 0)))
# #
# x_data = [[[1, 3, 2]]]
# with tf.Session() as sess:
#     print(sess.run(tf.argmax(x_data, 2)))