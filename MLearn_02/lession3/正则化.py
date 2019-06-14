# coding:utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

'''
正则化（规则化）缓解过度拟合
正则化在损失函数中引入模型复杂度指标，利用给w加权值，弱化训练数据的噪声
loss = loss(y与Y) + REGULARIZER * loss(w)
1:loss(w)=tf.contrib.layers.l1_regularizer(REGULARIZER)(w) lossl1(w)=sum(|wi|)
2:loss(w)=tf.contrib.layers.l2_regularizer(REGULARIZER)(w) lossl2(w)=sum(wi^2)

#把内容加到集合对应位置做加法
tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(REGULARIZER)(w)
loss = cem + tf.add_n(tf.get_collection('losses')
'''

one_size = 20
seed = 2202

rdm = np.random.RandomState(seed)
X = rdm.randn(500, 2)  # 生成500行2列的矩阵(x1,x2)
Y = [int(x1 * x1 + x2 * x2 < 2) for (x1, x2) in X]
Y_COLOR = [['RED' if y else 'BLUE'] for y in Y]
print(Y_COLOR)

# vstack(Y)把list转为numpy数据类型,reshape(-1, 1)保留原来结构转为1列
Y = np.vstack(Y).reshape(-1, 1)

plt.scatter(X[:, 0], X[:, 1], c=np.squeeze(Y_COLOR))  # squeeze函数把单行或列的矩阵转为向量
plt.show()

