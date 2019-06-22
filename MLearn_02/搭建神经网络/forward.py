# coding:utf-8
import tensorflow as tf

def get_weight(shape, regularizer):  # 计算w
    w = tf.Variable(tf.random_normal(shape), dtype=tf.float32)
    # 是否需要加入正则化
    if regularizer:
        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w

def get_bias(shape):   # 应该知道b的shape
    b = tf.Variable(tf.constant(0.01, shape=shape))
    return b

def forward(x_data, regularizer):  # 做前向传播运算
    w1 = get_weight([2, 11], regularizer)
    b1 = get_bias([11])
    a = tf.nn.relu(tf.matmul(x_data, w1) + b1)

    w2 = get_weight([11, 1], regularizer)
    b2 = get_bias([1])
    y = tf.matmul(a, w2) + b2
    return y
