import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import forward
import backward

TEST_INTERVAL_SECS = 5

def test(mnist):
    with tf.Graph().as_default() as g:
        x_data = tf.placeholder(tf.float32, [None, forward.INPUT_NODE])
        y_data = tf.placeholder(tf.float32, [None, forward.OUTPUT_NODE])
        y = forward.forward(x_data, None)

        # 实例化具有滑动平均的saver对象，从而在会话被加载时模型中的所有参数被赋值为各自的滑动平均值，增强模型的稳定性
        ema = tf.train.ExponentialMovingAverage(backward.MOVING_AVERAGE_DECAY)
        ema_restore = ema.variables_to_restore()
        saver = tf.train.Saver(ema_restore)

        # 计算模型在测试集上的准确率
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_data, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        while True:
            with tf.Session() as sess:
                # 加载指定路径下的ckpt
                ckpt = tf.train.get_checkpoint_state(backward.MODE_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict={x_data: mnist.test.images, y_data: mnist.test.labels})

                    #若模型不存在，则打印出模型不存在的提示，从而test()函数完成
                    print("第%s轮,test_accuracy=%g" % (global_step, accuracy_score))
                else:
                    print("没找到checkpoint文件")
                    return
            time.sleep(TEST_INTERVAL_SECS)
def main():
    mnist = input_data.read_data_sets("data/", one_hot=True)
    test(mnist)

if __name__ == "__main__":
    main()




