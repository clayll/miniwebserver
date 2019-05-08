import pandas as pd
import matplotlib as mpt
import numpy as np



data = np.genfromtxt("datas/data.csv",delimiter=",") #pd.read_csv("datas/data.csv", names=("x","y"))

x_data = data[:,0]
y_data = data[:,1]
k, b = 0.0, 0.0
lr = 0.01
m = len(x_data)

def createLossFuntion(k, b):
    loss = 0.0
    for i in range(m):
        loss += (y_data[i]-(k*x_data[i]+b))**2

    return loss/m/2.0

def gradient_computer(k,b):
    b_grad, k_grad =0.0 ,0.0
    for i in range(m):
        b_grad += (k*x_data[i]+b)  -y_data[i]
        k_grad += ((k*x_data[i]+b)  -y_data[i])*x_data[i]

    k = k - lr*k_grad/m
    b = b - lr*b_grad/m

    return k,b




if __name__ == '__main__':

    for i in range(50):
        k,b = gradient_computer(k, b)
        print("执行第{0}次，损失率为：{1},K：{2} b:{3}".format(i, createLossFuntion(k,b),k,b))


