import pandas as pd
import tensorflow as tf

# index = ['a','b']
# index2 = ["a","b"]
# pd1 = pd.Series(['hello',21],index=index)
# pd2 = pd.Series([3,9],index = index2)
# print(pd1*pd2)

a = tf.constant(123,dtype=tf.int32)
b = tf.constant(4,dtype=tf.int32)
rst = tf.add(a,b)
rst = tf.multiply(a,b)
sess = tf.Session()
print(sess.run(rst))