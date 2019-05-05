import tensorflow as tf

# 第一次尝试tensorflow
def first_01():
    a = tf.constant(3.0)
    b = tf.constant(4.0)

    sum = tf.add(a,b)
    sum1 = a+b
    g = tf.Graph()
    g1 = tf.get_default_graph()
    g1.as_default()
    with tf.Session() as session:
        x = session.run(sum)
        x1 = session.run(sum1)

        print(sum1.eval())
        print("session.graph  :",session.graph)
        print("g1:--",g1)

def graph_first():
    g = tf.Graph()
    with g.as_default():
        a = tf.constant(2)
        print(g)

def session_test():
    g = tf.Graph()
    with g.as_default():
        a = tf.constant(20)

    a1 = tf.constant(10)
    config = tf.ConfigProto(log_device_placement=True)

    with tf.Session() as session:
        print(a1.graph)
        print(a1.eval())

    with tf.Session(graph=g,config=config):
        print(a.graph)
        print(a.eval())

def tensor_test():
    plt = tf.placeholder(tf.int8,shape=(None,3))
    print(plt.shape)
    plt.set_shape([2,3])
    print(plt)

    reshpe = tf.reshape(plt,[3,2])
    print(reshpe)

    reshpe1 = tf.reshape(plt, [1, 6])
    print(reshpe1)

    s = tf.random_normal([3,3],mean=0,stddev=0.5)

    s1 = tf.ones([3,4])
    print(s)

    with tf.Session() as session:
        print(session.run([s,s1]))

"""
tensorboard    --logdir="./summary/01/" --host 127.0.0.1
"""
def tensorbord_test():
    a = tf.constant(10,name="a")
    array1 = tf.random_normal([4,3],mean=32,stddev=0.9)
    ar2 = tf.Variable(tf.random_normal([3,3],mean=0,stddev=0.5))

    initVar = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(initVar)
        sess.run([a,array1,ar2])
        summaryfile = tf.summary.FileWriter("./summary/01/",graph=sess.graph)
        print(summaryfile)

def line_regression_test():
    # y = 0.7x+0.8
    # 数据的准备
    with tf.variable_scope("data"):
        x_data = tf.random_normal(shape=(1000,1),mean=1.75,stddev=0.5,name="x_data")
        y_true = tf.matmul(x_data,[[0.7]])+0.8

    with tf.variable_scope("model"):
        # 数据的权重
        weight = tf.Variable([[0.1]],name="w",dtype=tf.float32)
        # 数据的误差
        bias = tf.Variable(0.0,dtype=tf.float32)
        # 预测值
        y_prodict = tf.matmul(x_data,weight)+bias

    with tf.variable_scope("loss"):
        # 平方差中的最小值，最小数
        loss = tf.reduce_mean(tf.square(y_true-y_prodict))


    with tf.variable_scope("optimizer"):
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    tf.summary.scalar("loss", loss)
    tf.summary.histogram("weight",weight)
    merge = tf.summary.merge_all()
    init_op = tf.global_variables_initializer()
    saver = tf.train.Saver()
    # 开启变量
    with tf.Session() as sess:
        sess.run(init_op)
        fileWriter = tf.summary.FileWriter("./summary/01/", graph=sess.graph)
        print("初始化的权重：{0},初始化的误差：{1}".format(weight.eval() ,bias.eval()))
        saver.restore(sess, './ckpt/01/')
        for i in range(400):
            sess.run(train_op)
            mersummy = sess.run(merge)
            fileWriter.add_summary(mersummy,i)
            print("第{0}次运行，运行后的权重：{1},初始化的误差：{2}".format(i,weight.eval() ,bias.eval()))

        saver.save(sess,'./ckpt/01/')



if __name__ == '__main__':
    # first_01()
    #
    # graph_first()
    # session_test()
    # tensor_test()

    line_regression_test()
    # y = tf.constant([[1,2,3,4,5]],shape=(5,1),dtype=tf.float16)
    # z = tf.constant([[0.7]],shape=(1,1),dtype=tf.float16)
    # with tf.Session() as sess:
    #     print(sess.run(tf.matmul(y,z)))