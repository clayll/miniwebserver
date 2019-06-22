import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import forward
import os

ONE_SIZE = 200   # 一次喂入的数据个数
LEARNING_RATE_BASE = 0.1
LEARNING_RATE_DECAY = 0.99

REGULARIZER = 0.0001
STEPS = 50000   # 训练次数
MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH = "./model/"
MODEL_NAME = "mnist_model"

def backward(mnist):
    # 用placeholder给训练数据x_data和标签y_data占位
    x_data = tf.placeholder(tf.float32, [None, forward.INPUT_NODE])
    y_data = tf.placeholder(tf.float32, [None, forward.OUTPUT_NODE])

    # 调用forward文件中的前向传播过程forword()函数，并设置正则化，计算训练数据集上的预测结果y
    y = forward.forward(x_data, REGULARIZER)

    # 当前计算轮数计数器赋值，设定为不可训练类型
    global_step = tf.Variable(0, trainable=False)

    # 调用包含所有参数正则化损失的损失函数loss
    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_data, 1))
    cem = tf.reduce_mean(ce)
    loss = cem + tf.add_n(tf.get_collection('losses'))

    # 设定指数衰减学习率learning_rate
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        mnist.train.num_examples / ONE_SIZE,
        LEARNING_RATE_DECAY,
        staircase=True)

    # 使用梯度衰减算法对模型优化，降低损失函数
    # train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    train_step = tf.train.MomentumOptimizer(learning_rate, 0.9).minimize(loss, global_step=global_step)
    # train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss, global_step=global_step)

    # 定义参数的滑动平均
    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    ema_op = ema.apply(tf.trainable_variables())

    with tf.control_dependencies([train_step, ema_op]):
        train_op = tf.no_op(name="train")

    saver = tf.train.Saver()

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)

        for count in range(1, STEPS):
            xx, yy = mnist.train.next_batch(ONE_SIZE)
            _, now_loss, step = sess.run([train_op, loss, global_step], feed_dict={x_data: xx, y_data: yy})
            if count % 1000 == 0:
                print("第%s轮的损失值为%s" % (step, now_loss))
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)
def main():
    minst = input_data.read_data_sets("./data/", one_hot=True)
    backward(mnist=minst)

if __name__ == "__main__":
    main()





