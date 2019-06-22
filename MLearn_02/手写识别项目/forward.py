import tensorflow as tf

INPUT_NODE = 784   # 输入节点784列
OUTPUT_NODE = 10   # 输出节点10列
LAYER1_NODE = 500  # 第一次神经网络的列数

def get_weight(shape, regularizer):
    # 使用tf.truncated_normal的输出是不可能出现[-2,2]以外的点的数据
    w = tf.Variable(tf.truncated_normal(shape, stddev=0.1))
    if regularizer:
        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(regularizer)(w))

    return w

def get_bias(shape):
    return tf.Variable(tf.zeros(shape=shape))

def forward(x_data, regularizer):
    w1 = get_weight([INPUT_NODE, LAYER1_NODE], regularizer)
    b1 = get_bias(LAYER1_NODE)
    a = tf.nn.relu(tf.matmul(x_data, w1) + b1)  # 激活函数

    w2 = get_weight([LAYER1_NODE, OUTPUT_NODE], regularizer)
    b2 = get_bias(OUTPUT_NODE)
    y = tf.matmul(a, w2) + b2

    return y
