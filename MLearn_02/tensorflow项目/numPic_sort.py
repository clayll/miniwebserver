from PIL import Image
import tensorflow as tf
import numpy as np
import NN_mnist_project


PIC_WIDTH = 28
PIC_HIGHT = 28

def restore_model(testPicArr):

    x_data = tf.placeholder(shape=(None, 784), dtype=tf.float32)
    y_ = NN_mnist_project.forword( )
    preValue = tf.argmax(y_,1)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state("Model/")
        if ckpt:
            saver.restore(sess,ckpt.model_checkpoint_path)
            preValue = sess.run(preValue, feed_dict={x_data: testPicArr})
            print(preValue)
        else:
            print("没有找到模型")




def preprocessPic(picPath):
    try:
        img = Image.open(picPath)
        reImg = img.resize((PIC_WIDTH,PIC_HIGHT), 1)
        # reImg.save("pic_fit/33.png")

        # Image.Image.resize()

        img_arr = np.array(reImg.convert("L"))
        threshold = 50  # 设置一个阈值
        for i in range(PIC_WIDTH):
            for j in range(PIC_HIGHT):
                # 颜色逆转（通过图片像素特征值把图片像素黑白互换）
                img_arr[i][j] = 255 - img_arr[i][j]
                if img_arr[i][j] < threshold:
                    img_arr[i][j] = 0  # 变成纯黑色
                else:
                    img_arr[i][j] = 255  # 变成纯白色
        nm_arr = img_arr.reshape(1, 784)  # 把shape(28, 28)转为（1， 748）
        nm_arr = nm_arr.astype(np.float32)  # 变为浮点数
        img_ready = np.multiply(nm_arr, 1.0 / 255.0)  # 把0-255的浮点数变为0-1之间的浮点数

        return img_ready

    except Exception as ex:
        print(ex)
        print("没有找到图片")


if __name__ == "__main__":
    testPic =  preprocessPic("pic/33.png")
    restore_model(testPic)