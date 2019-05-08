import pandas as pd

data = pd.read_csv("datas/data.csv", names=("x","y"))
x_data = data.ix[:,"x"]
y_data = data.ix[:,"y"]
k, b = 0.0, 0.0
lr = 0.01
m = len(x_data)

def createLossFuntion(k, b ):
    loss = 0.0
    for i in range(m):
        loss += (y_data.ix[i,"y"]-(k*x_data.ix[i,"x"]+b))**2

    return loss/m/2.0

def gradient_computer(k,b):
    for i in range(50):
        k += k - lr*k
        b += b - lr

    print("执行第{0}次，损失率为：{1}", i, createLossFuntion(k / m, b / m))


if __name__ == '__main__':
    print(createLossFuntion(k,b))
    gradient_computer(k,b)


