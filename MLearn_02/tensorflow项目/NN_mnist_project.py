import input_data
import tensorflow as tf


ds = input_data.read_data_sets("MNIST_data",one_hot=True)

x_train = ds.train.images
y_train = ds.train.labels

x_test = ds.test.images
y_test = ds.test.labels

# print(x_train[0:1],y_train[0:1])

#定义初始化数据
x = tf.placeholder(shape=(None,784),dtype=tf.float32)
y = tf.placeholder(shape=(None,10),dtype=tf.float32)


# w0 = tf.Variable(tf.zeros((784,784)),dtype=tf.float32)
# b0 = tf.Variable(tf.zeros([784]))

w = tf.Variable(tf.zeros((784,10)),dtype=tf.float32)
b = tf.Variable(tf.zeros([10]))

# # 第一层的结果
# y0_ = tf.matmul(x,w0)+b0
#
# corss_entroy0 = tf.nn.softmax(y0_)

# 第二层的结果
y_ = tf.matmul(x,w)+b

corss_entroy = tf.nn.softmax(y_)

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy  = tf.reduce_mean(tf.cast(correct_prediction,dtype=tf.float32))

loss = -tf.reduce_sum(y* (tf.log(corss_entroy)))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)


with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    start = 0
    end = 500
    endMax = x_train.shape[0]
    while True:
        if end > endMax:
            break
        sess.run(train_step,feed_dict={x : x_train[start:end], y : y_train[start:end]})
        now_loss = sess.run(loss, feed_dict={x: x_train[start:end], y: y_train[start:end]})
        print("%s第%s轮训练后的now_loss值：%s " % (start,end, now_loss))
        if end %  2000 == 0 :
            print("准确率是：", sess.run(accuracy, feed_dict={x: x_train[start:end], y: y_train[start:end]}))
        start+= 500
        end +=  500
    # y_prodict = sess.run(corss_entroy,feed_dict={x: x_test,y: y_test})
    # print("准确率是：", sess.run(accuracy, feed_dict={x: x_test,y: y_test}))
    #
    # for i in range(1000):
    #     batch_xs, batch_ys = ds.train.next_batch(500)
    #     sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    #     now_loss = sess.run(loss, feed_dict={x: batch_xs, y: batch_ys})
    #     print("正确率是：",sess.run(accuracy , feed_dict={x: batch_xs, y: batch_ys}))
    #     print("第%s轮训练后的now_loss值：%s " % (i, now_loss))