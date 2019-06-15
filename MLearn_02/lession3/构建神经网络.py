import tensorflow as tf
import numpy as np
import random

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))   # in_size行，out_size列
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.11)           # 1行 out_size列个0.11

    Wx_plus_b = tf.matmul(inputs, Weights) + biases  # inputs的列是in_size，Weights的行是in_size

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# 生成一个500行1列的数据，范围在[-1, 1)
#x_data = np.random.uniform(low=-1, high=1, size=(500, 1))

x_data = np.array([[2, 3, 4, 5, 6]]).T
print(x_data)
# 值分布在0到0.05上的正态分布上的值
noise = np.random.uniform(0, 0.05, x_data.shape)
print(noise)
# y_data = 矩阵x_data的平方 - 0.5
# y_data = np.square(x_data) - 0.5





