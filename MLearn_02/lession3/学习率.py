# coding:utf-8
# learing_rate(每次参数更新的幅度）
# w(n+1) = w(n) - learning_rate * loss'(w)(损失函数的梯度）
#print(1.4 - 0.2*(2 * 1.4 + 2))

'''
我们假定有损失函数loss = (w + 1)^2
则loss'(w) = 2w + 2

假定w初始参数为3，学习率为0.2，则：

w = w(上一次的） - 学习率*（2 * w(上一次的） + 2）

第1次的w值： 参数w为3， 则计算结果为：3 - 0.2*(2 * 3 + 2) = 1.4
第2次的w值： 参数w为1.4 则计算结果为：1.4 - 0.2*(2 * 1.4 + 2) = 0.43999994
第3次的w值： 参数w为0.43999994   则计算结果为：0.43999994 - 0.2*(2 * 0.43999994 + 2) = -0.13600004
第n次的w值.....，
最后w求值为-1是我们要的值（如图）
'''

# 代码示例
# 设损失函数loss = (w + 1)^2， w初始化为3，利用反向传播求w（最小化loss对应的w值）
import tensorflow as tf
learning_rate = 0.537203  # 设置太大震荡不收敛，太小收敛慢
counts = 50  # 训练50轮
w = tf.Variable(tf.constant(13.0))  # w初始化为3

loss = tf.square(w + 1)  # 损失函数loss
# 反向传播方法
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for count in range(1, counts + 1):
        sess.run(train_step)
        now_w = sess.run(w)
        now_loss = sess.run(loss)
        print("第%s轮now_w:%s, now_loss:%s" % (count, now_w, now_loss))
