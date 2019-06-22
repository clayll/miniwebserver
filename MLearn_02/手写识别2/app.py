import tensorflow as tf
import numpy as np
from PIL import Image
import backward
import forward

PIC_WIDTH = 28
PIC_HIGHT = 28

def restore_model(testPicArr):
    with tf.Graph().as_default() as g:
        x_data = tf.placeholder(tf.float32, [None, forward.INPUT_NODE])
        y = forward.forward(x_data, None)
        preValue = tf.argmax(y, 1)

        variable_averages = tf.train.ExponentialMovingAverage(backward.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(backward.MODEL_SAVE_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
                preValue = sess.run(preValue, feed_dict={x_data: testPicArr})

                return preValue
            else:
                print("没找到文件")
                return -1

def pre_pic(picpath):
    try:
        img = Image.open(picpath)
    except:
        print("没有该图片")
        return
    # 调整图片大小消除锯齿
    reImg = img.resize((PIC_WIDTH, PIC_HIGHT), Image.ANTIALIAS)
    # 把图片变成灰度图，并把图片转为矩阵
    img_arr = np.array(reImg.convert("L"))
    threshold = 50  # 设置一个阈值

    for i in range(PIC_WIDTH):
        for j in range(PIC_HIGHT):
            # 颜色逆转（通过图片像素特征值把图片像素黑白互换）
            img_arr[i][j] = 255 - img_arr[i][j]
            if img_arr[i][j] < threshold:
                img_arr[i][j] = 0    # 变成纯黑色
            else:
                img_arr[i][j] = 255  # 变成纯白色

    nm_arr = img_arr.reshape(1, 784)    # 把shape(28, 28)转为（1， 748）
    nm_arr = nm_arr.astype(np.float32)  # 变为浮点数
    img_ready = np.multiply(nm_arr, 1.0 / 255.0)  # 把0-255的浮点数变为0-1之间的浮点数

    return img_ready

def application():
    testNum = input("请输入要检测数字图片的个数：")
    for i in range(int(testNum)):
        testPicPath = input("输入数字图片所在路径")

        # 预处理图片为（1, 784）的矩阵
        testPicArr = pre_pic(testPicPath)

        preValue = restore_model(testPicArr)
        print("被测的数据是：", preValue)

if __name__ == '__main__':
    application()