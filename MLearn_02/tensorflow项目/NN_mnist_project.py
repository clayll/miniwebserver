import input_data
import tensorflow as tf


ds = input_data.read_data_sets("MNIST_data",one_hot=True)

x_train = ds.train.images
y_train = ds.train.labels

# print(x_train[0:1],y_train[0:1])

#定义初始化数据
x = tf.placeholder(shape=(None,784),dtype=tf.float32)
y = tf.placeholder(shape=(None,10),dtype=tf.float32)

w = tf.Variable(tf.random_normal((784,10)),dtype=tf.float32)
b = tf.Variable(tf.random_normal((1,10)),dtype=tf.float32)
y_ = tf.matmul(x,w)+b

corss_entroy = tf.nn.softmax(y_)

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy  = tf.reduce_mean(tf.cast(correct_prediction,dtype=tf.float32))

loss = tf.reduce_sum(y* (-tf.log(corss_entroy)))
train_step = tf.train.GradientDescentOptimizer(0.0000001).minimize(loss)


with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    start = 0
    end = 500
    endMax = x_train.shape[0]
    while True:
        if end > endMax:
            break


        sess.run(train_step,feed_dict={x : x_train[start:end], y : y_train[start:end]} )
        now_loss = sess.run(loss, feed_dict={x: x_train[start:end], y: y_train[start:end]})
        print("第%s轮训练后的now_loss值：%s " % (end, now_loss))
        print("正确率是：", sess.run(accuracy, feed_dict={x: x_train[start:end], y: y_train[start:end]}))
        start = start+end
        end = end + 500
    #
    # for i in range(1000):
    #     batch_xs, batch_ys = ds.train.next_batch(500)
    #     sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    #     now_loss = sess.run(loss, feed_dict={x: batch_xs, y: batch_ys})
    #     print("正确率是：",sess.run(accuracy , feed_dict={x: batch_xs, y: batch_ys}))
    #     print("第%s轮训练后的now_loss值：%s " % (i, now_loss))