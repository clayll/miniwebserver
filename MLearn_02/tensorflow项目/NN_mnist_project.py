import input_data
import tensorflow as tf
import numpy as np


LEARNING_RATE_BASE = 0.001   # 学习率
LEARNING_RATE_DECAY = 0.99
step = 10000
ds = input_data.read_data_sets("MNIST_data",one_hot=True)
batch_size = 50
DATAS_COUNT = 55000



x_test = ds.test.images
y_test = ds.test.labels
# print(x_train[0:1],y_train[0:1])

# 定义初始化数据
x = tf.placeholder(shape=(None, 784), dtype=tf.float32)
y = tf.placeholder(shape=(None, 10), dtype=tf.float32)

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

def forword():
    w0 = get_w_variable((784, 500), 0.0001)
    b0 = bias_variable((1, 500))

    w = get_w_variable((500, 10), 0.0001)
    b = bias_variable((1, 10))

    # 第一层的结果
    y0_ = tf.matmul(x, w0) + b0

    corss_entroy0 = tf.nn.relu(y0_)

    # 第二层的结果
    y_ = tf.matmul(corss_entroy0, w) + b
    return y_

def get_w_variable(size,regularization):
    w = tf.Variable(tf.truncated_normal(size,mean=0,stddev=0.1))
    if regularization:
        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(regularization)(w))
    return w


def NN_test():


    y_ = forword()
    corss_entroy = tf.nn.softmax(y_)

    correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
    accuracy  = tf.reduce_mean(tf.cast(correct_prediction,dtype=tf.float32))


    global_step = tf.Variable(0, trainable=False)
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        100,
        LEARNING_RATE_DECAY,
        staircase=False)
    regu_loss = tf.add_n(tf.get_collection('losses'))
    loss = -tf.reduce_sum(y* (tf.log(corss_entroy))) + regu_loss
    # loss = -tf.reduce_sum(y * (tf.log(corss_entroy)))
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)


    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        saver = tf.train.Saver()

        for i in range(step):
            x_train,y_train = ds.train.next_batch(batch_size)
            sess.run(learning_rate,feed_dict={global_step:i})
            sess.run(train_step,feed_dict={x : x_train, y : y_train})
            now_loss = sess.run(loss, feed_dict={x : x_train, y : y_train})
            if i % 100 == 0:
                print("第%s轮训练后的now_loss值：%s " % (i , now_loss))
            if i % 2000 == 0:
                saver.save(sess,"model/"+ 'model.ckpt',global_step=i+1)
            # if end %  2000 == 0 :
            #     print("准确率是：", sess.run(accuracy, feed_dict={x: x_train[start:end], y: y_train[start:end]}))

        # y_prodict = sess.run(corss_entroy,feed_dict={x: x_test,y: y_test})
        print("准确率是：", sess.run(accuracy, feed_dict={x: x_test,y: y_test}))
        #
        # for i in range(1000):
        #     batch_xs, batch_ys = ds.train.next_batch(500)
        #     sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
        #     now_loss = sess.run(loss, feed_dict={x: batch_xs, y: batch_ys})
        #     print("正确率是：",sess.run(accuracy , feed_dict={x: batch_xs, y: batch_ys}))
        #     print("第%s轮训练后的now_loss值：%s " % (i, now_loss))

def test():
    one_img = np.array([[[[3, 3, 2, 1, 0],
                          [0, 0, 1, 3, 1],
                          [3, 1, 2, 2, 3],
                          [2, 0, 0, 2, 2],
                          [2, 0, 0, 0, 1]]]])

    # 将二维数据转化为四维数据
    one_data = tf.constant(one_img)

    # (1, 1, 5, 5) 成功转化为四维数据
    # print(one_img.shape)

    # 卷积conv2d需要输入四维数据，其中输入和输出均为单通道，卷积核为3
    # conv = tf.nn.conv2d(one_img)

    # print(conv)

    a = np.random.randint(low=1, high=10, size=32)
    a = a.reshape((1, 4, 4, 2))
    print(a)

    a = tf.constant([
        [[1.0, 2.0, 3.0, 4.0],
         [5.0, 6.0, 7.0, 8.0],
         [8.0, 7.0, 6.0, 5.0],
         [4.0, 3.0, 2.0, 1.0]],
        [[4.0, 3.0, 2.0, 1.0],
         [8.0, 7.0, 6.0, 5.0],
         [1.0, 2.0, 3.0, 4.0],
         [5.0, 6.0, 7.0, 8.0]]
    ])

    a = tf.reshape(a, [1, 4, 4, 2])

    pooling = tf.nn.max_pool(a, [1, 2, 2, 1], [1, 2, 2, 1], padding='SAME')
    with tf.Session() as sess:
        print("image:")
        image = sess.run(a)
        print(image)
        print("reslut:")
        result = sess.run(pooling)
        print(result)
        print(result.shape)

def CNN_test():
    # 第一层卷积
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    x_image = tf.reshape(x_train, [-1, 28, 28, 1])

    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)
    # 第二层卷积
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])

    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    # 密集层
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    # dropout层
    # keep_prob = tf.placeholder("float")
    # h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])

    # y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
    y_conv = tf.nn.softmax(tf.matmul(h_fc1, W_fc2) + b_fc2)

    cross_entropy = -tf.reduce_sum(y_train * tf.log(y_conv))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        for i in range(20000):
            batch = ds.train.next_batch(50)
            if i % 100 == 0:
                train_accuracy = accuracy.eval(feed_dict={
                    # x: batch[0], y: batch[1], keep_prob: 1.0})
                    x: batch[0], y: batch[1]})
                print
                ("step %d, training accuracy %g" % (i, train_accuracy))
            # train_step.run(feed_dict={x: batch[0], y: batch[1], keep_prob: 0.5})

            train_step.run(feed_dict={x: batch[0], y: batch[1]})
        print
        ("test accuracy %g" % accuracy.eval(feed_dict={
            # x: ds.test.images, y: ds.test.labels, keep_prob: 1.0})

            x: ds.test.images, y: ds.test.labels}))

def NN_Predict():
    y_ = forword()
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    saver = tf.train.Saver()
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        ckpt = tf.train.get_checkpoint_state("model/")
        if  ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)

            print(sess.run(accuracy,feed_dict={x:ds.test.images,y:ds.test.labels}))


if __name__ == '__main__':
    NN_Predict()