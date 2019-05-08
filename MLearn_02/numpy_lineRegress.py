import matplotlib.pyplot as plt
import numpy as np



data = np.genfromtxt("datas/data.csv",delimiter=",") #pd.read_csv("datas/data.csv", names=("x","y"))

x_data = data[:,0]
y_data = data[:,1]
k, b = 0.0, 0.0
lr = 0.0001
m = len(x_data)
grad_count = 50

plt.scatter(x_data,y_data)
plt.show()

def createLossFuntion(k, b):
    loss = 0.0
    for i in range(m):
        loss += (y_data[i]-(k*x_data[i]+b))**2

    return loss/float(m)/2.0

def gradient_computer(k,b):
    for j in range(grad_count):
        b_grad, k_grad = 0.0, 0.0
        for i in range(m):
            # b_grad += ((k*x_data[i]+b)  -y_data[i])/m
            # k_grad += (((k*x_data[i]+b)  -y_data[i])*x_data[i])/m
            b_grad += (1 / m) * (((k * x_data[i]) + b) - y_data[i])
            k_grad += (1 / m) * x_data[i] * (((k * x_data[i]) + b) - y_data[i])

        b = b - (lr * b_grad)
        k = k - (lr*k_grad)

        if j % 5 == 0:
            plt.plot(x_data,y_data,'b.')
            plt.plot(x_data,x_data*k+b,'r')
            plt.show()
        print("第{0}次，k:{1}，b：{2}".format(j,k,b))


    return k,b




if __name__ == '__main__':
    print("初始损失率：{0}".format(createLossFuntion(k, b)))
    k,b = gradient_computer(k, b)
    print("损失率为：{0},K：{1} b:{2}".format(createLossFuntion(k,b),k,b))


