import pandas as pd
import tensorflow as tf
import numpy as np

# index = ['a','b']
# index2 = ["a","b"]
# pd1 = pd.Series(['hello',21],index=index)
# pd2 = pd.Series([3,9],index = index2)
# print(pd1*pd2)
#
# a = tf.constant(123,dtype=tf.int32)
# b = tf.constant(4,dtype=tf.int32)
# rst = tf.add(a,b)
# rst = tf.multiply(a,b)
# sess = tf.Session()
# print(sess.run(rst))

a = np.array([[1,3,1],[5,5,2],[15,8,9],[20,44,12]])
# probs = a / np.sum(a, axis=1, keepdims=True)  # [N x K]
# print(probs)
y= np.array([0,1,0,1])
# print(probs[range(4),y])

probs = np.exp(a - np.max(a, axis=1, keepdims=True))

probs /= np.sum(probs, axis=1, keepdims=True)
loss = -np.sum(np.log(probs[np.arange(4), y])) / 4
print(np.log(probs[np.arange(4), y]))
print(loss)



