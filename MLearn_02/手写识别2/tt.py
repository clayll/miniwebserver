from PIL import Image
import numpy as np

PIC_WIDTH = 28
PIC_HIGHT = 28

filepathok = "d:/ok/"

def doImage(picpath):
    img = Image.open(picpath)
    # 调整图片大小消除锯齿
    reImg = img.resize((PIC_WIDTH, PIC_HIGHT), Image.ANTIALIAS)
    reImg.save(filepathok + "调整/" + picpath)

    # 把图片变成灰度图，并把图片转为矩阵
    img_arr = np.array(reImg.convert("L"))

    reImg = Image.fromarray(img_arr)
    reImg.save(filepathok + "灰度/" + picpath)
    threshold = 50  # 设置一个阈值

    for i in range(PIC_WIDTH):
        for j in range(PIC_HIGHT):
        # 颜色逆转（通过图片像素特征值把图片像素黑白互换）
            img_arr[i][j] = 255 - img_arr[i][j]
            # if img_arr[i][j] < threshold:
            #     img_arr[i][j] = 0    # 变成纯黑色
            # else:
            #     img_arr[i][j] = 255  # 变成纯白色

    nm_arr = img_arr.reshape(1, 784)  # 把shape(28, 28)转为（1， 748）

    # #nm_arr = nm_arr.astype(np.float32)  # 变为浮点数
    # img_ready = np.multiply(nm_arr, 1.0 / 255.0)  # 把0-255的浮点数变为0-1之间的浮点数

    reImg = Image.fromarray(img_arr)
    reImg.save(filepathok + "像素互换/" + picpath)

while True:
    pass
    filepath = input("输入图片路径：")
    doImage(filepath)

