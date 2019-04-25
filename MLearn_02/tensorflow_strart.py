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


if __name__ == '__main__':
    # first_01()
    #
    # graph_first()
    # session_test()
    # tensor_test()
    tensorbord_test()