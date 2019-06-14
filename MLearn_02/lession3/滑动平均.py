'''
滑动平均（也叫作影子值）
该值记录了每个参数变化后一段时间内过往值的平均，改值像变化参数的影子一样
追随着该参数
影子值=衰减率*影子值 + （1-衰减率）*参数；影子初值等于参数初值
衰减率=min(MOVING_AVERAGE_DECAY, 1+轮数/10+轮数)
'''

'''
设：MOVING_AVERAGE_DECAY为0.99，参数w1为0，
1.当轮数global_step为0，w1的滑动平均值为0，参数w1更新为1则：
w1的影子值=min(0.99, 1+0/10+0)*0 + (1-min(0.99, 1+0/10+0))*1 = 0.9
2.当轮数global_step为100，参数w1更新为10则：
w1的影子值=min(0.99, 1+100/10+100)*0.9 + (1-min(0.99, 1+100/10+100))*10 = 1.644
'''

import tensorflow as tf

# 定义变量和滑动平均类
# 定义变量初始值为0.0，我们不断更新w1参数，优化w1参数，滑动平均值即是w1的影子值
w1 = tf.Variable(0.0)  # w1初始值为0
global_step = tf.Variable(0, trainable=False)  # 轮数初始值为0
MOVING_AVERAGE_DECAY为0 = 0.99  # 衰减率一般是个比较大的常量
ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY为0, global_step)

# ema.apply后的括号里是更新列表，每次运行sess.run(ema_op)时，对更新列表中的元素
# 求滑动平均值
# 在实际应用中会使用tf.trainable_variables()自动将所有待训练
# 的参数汇总为列表：ema_op = ema.apply([w1])
ema_op = ema.apply(tf.trainable_variables())

#2.查看不同迭代中变量取值的变化
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    # 用ema.average(w1)获取w1的滑动平均值,打印出当前参数w1和w1滑动平均值
    print(sess.run([w1, ema.average(w1)]))

    # 参数w1的值赋值为1
    sess.run(tf.assign(w1, 1))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    # 更新step为100，w1为10
    sess.run(tf.assign(global_step, 100))
    sess.run(tf.assign(w1, 10))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    # 每次sess.run会更新一次w1的滑动平均值
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))
