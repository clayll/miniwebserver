import numpy as np
import tensorflow as tf



'''
numpy.random的random函数
1.生成[0.0, 1.0)的随机数。注意区间是左闭右开，0.0 <= data < 1.0。
2.生成的是浮点数。
3.参数size可以用于指定生成随机数的个数和形状。
'''

#x_data = np.random.random(size=9)       # 和size=(9,)一样，shape是(9,),非矩阵
#print(x_data.shape)
#print(x_data)
# print(x_data.T)
#
# x_data = np.random.random(size=(3, 4))  # 和size=(3, 4)一样，shape是(3, 4),矩阵3行4列
# print(x_data.shape)
# print(x_data)
# print(x_data.T)

'''
numpy.random的rand函数
1.生成[0.0, 1.0)的随机数。注意区间是左闭右开，0.0 <= data < 1.0。
2.生成的是浮点数。
3.参数size可以用于指定生成随机数的个数和形状。
返回值：
    ndarray类型，其形状和参数size中描述一致。
'''

# x_data = np.array(np.random.rand(9,))# 类似x_data = np.random.random(size=9)
# x_data = np.random.rand(1, 10)       # 生成矩阵 1 行 10列，数值范围在[0, 1)
#
# print(x_data)
# x_data = x_data.T
# print(x_data)

'''
numpy的random.uniform函数
功能：
    从一个均匀分布[low,high)中随机采样float类型，注意定义域是左闭右开，即包含low，不包含high.
参数介绍: 
    low: 采样下界，float类型，默认值为0；
    high: 采样上界，float类型，默认值为1；
    size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n), 则输出m*n个样本，缺省时输出1个值。
返回值：
    ndarray类型，其形状和参数size中描述一致。
'''

# 一种生成某个范围的随机数（tensor类）


# x_data = np.random.uniform(low=-3, high=3, size=(1, 10))  # 生成某个范围内随机数组
# print(x_data)

# import matplotlib.pyplot as plt
# import numpy as np
#
#s = np.random.uniform(0, 1, size=(2, 4))    # 产生shape(2, 4)个[0,1)的数
# count, bins, ignored = plt.hist(s, 12, density=True)
# plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
# plt.show()

'''
numpy的random.normal函数
生成的值符合正态分布，有方差和均值
'''
# import matplotlib.pyplot as plt
# import numpy as np
# #
# s = np.random.normal(0, 2, size=(120, ))    # 产生1200个数正态分布
# print(s)
# count, bins, ignored = plt.hist(s, 12, density=True)
# plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
# plt.show()

'''
说明：
TF
tf.random_normal()函数用于从服从指定正太分布的数值中取出指定个数的值。
tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)

NP
np.random.normal()给出均值为loc，标准差为scale的高斯随机数.
numpy.random.normal(loc=0.0, scale=1.0, size=None)

所谓正态分布=高斯分布，所以二者一回事 mean=loc=均值（或称期待值） 
stddev=scale=标准差 shape=size=输出形状，二者在处理这个参数时候(a,b)=[a,b],
其中np的normal对参数格式要求更灵活一些。
比如创建随机数的一行两列数组：
np.random.normal([2])=np.random.normal((2))=np.random.normal(0，1，2)注意最后一种用法必须带上前面两个参数，否则传递参数时候会把2当作均值传递
而tf的random_normal对shape的要求不能是数字，必须为[]或()格式
 
'''

# 均匀分布
# data = np.random.uniform(low=1, high=5, size=15)  # size可以写成数字和size=(15,)一样
# print(data)

# data = tf.random_uniform(shape=(15, 2),  minval=1, maxval=5)  # shap要写成list或元组形式，不能是数字
# sess = tf.Session()
# init = sess.run(data)
# print(init)

# 正态分布
#
# data = np.random.normal(loc=0.0, scale=1.0, size=15)  # size可以写成数字和size=(15,)一样
# print(data)
#

# data = tf.random_normal(shape=(15, ),  mean=0.0, stddev=2.0)  # shape要写成list或元组形式，不能是数字
# sess = tf.Session()
# init = sess.run(data)
# print(init)

#//////////////////////////////
# tf和numpy还有一些函数也可以生成定值
# data = tf.zeros(shape=(5, 2))  # 5行2列全0矩阵
# sess = tf.Session()
# init = sess.run(data)
# print(init)
#
# data = tf.ones(shape=(1, 5))  # 1行5列全0矩阵
# sess = tf.Session()
# init = sess.run(data)
# print(init)
# #
# data = tf.fill((5,), 8)  # 5个元素的向量，值全为8
# sess = tf.Session()
# init = sess.run(data)
# print(init)
#
# data = tf.constant([2, 3, 3])  # 生成常量

#//////////////////////////
# x_data = np.linspace(-3, 3, 9)  # 生成9个数范围在-3 到 3之间
# print(x_data)

# x_data = np.linspace(-3, 3, 9)[:, np.newaxis]  # 生成9个数范围在-3 到 3之间转为9行一列的矩阵
# print(x_data)

# X = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(X[:, [1, 3]])  # 取每行的第[1, 3]列组成一个矩阵

# 注意python的random模块只能生成随机数字，生成数组用numpy模块的random
