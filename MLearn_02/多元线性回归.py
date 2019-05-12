from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


class MultiRegression():
    def __init__(self):
        self.data = np.genfromtxt("./datas/Delivery.csv",delimiter=",")
        self.x_data = self.data[:,:-1]
        self.y_data = self.data[:,-1]
        self.count = float(len(self.y_data))
        self.lr = 0.0001
        self.k1,self.k2,self.b =0,0,0
        self.gradientCount = 3000


    # 2个特征值的模型，线性回归
    def modelType(self):
        loss = 0

        for i in range(len(self.x_data)):
            loss += 1/self.count*((self.y_data[i] - (self.k1*self.x_data[i,0]+self.k2*self.x_data[i,1]+self.b))**2)

        return loss

    # 自己实现梯度下降模型
    def selfGradient(self):
        for j in range(self.gradientCount):
            k1_grad,k2_grad,b_grad = 0, 0 , 0
            for i in range(len(self.x_data)):

                k1_grad += (1/self.count)*self.x_data[i,0]*(((self.k1*self.x_data[i,0]+self.k2*self.x_data[i,1]+self.b) - self.y_data[i] ))
                k2_grad += -((self.y_data[i] - (self.k1 * self.x_data[i,0] + self.k2 * self.x_data[i,1] + self.b))) * self.x_data[i,1]
                b_grad += -((self.y_data[i] - (self.k1 * self.x_data[i,0] + self.k2 * self.x_data[i,1] + self.b)))

            self.k1 = self.k1 - (self.lr*k1_grad)
            self.k2 = self.k2 - (1 / self.count * self.lr * k2_grad)
            self.b = self.b - (1 / self.count * self.lr * b_grad)




    def run(self):
        # plt.subplot(2,1,1)
        # plt.scatter(self.x_data[:,0],self.y_data ,c= 'r')
        # plt.subplot(2, 1, 2)
        # plt.scatter(self.x_data[:, 1], self.y_data, c='c')
        # plt.show()
        loss1 = self.modelType()
        print("loss:{0},k1:{1},k2:{2},k3:{3}".format(loss1,self.k1,self.k2,self.b))
        self.selfGradient()
        print("loss:{0},k1:{1},k2:{2},k3:{3}".format(self.modelType(), self.k1, self.k2, self.b))
        axes = plt.subplot(1, 1, 1, projection="3d" )
        axes.scatter(self.x_data[:, 0], self.x_data[:, 1], self.y_data, c="r", marker="o",s=10)


        x1 = self.x_data[:,0]
        x2 = self.x_data[:,1]
        x1, x2 = np.meshgrid(x1, x2)
        z = self.k1 * x1 + self.k2 * x2 + self.b



        # print(x1,x2,z,x1.shape,x2.shape,z.shape)
        axes.plot_surface(x1,x2 ,z)
        axes.set_xlabel('Miles')
        axes.set_ylabel('Num of Deliveries')
        axes.set_zlabel('Time')
        plt.show()

    def test(self):
        # a1 = np.array([[1, 2, 3], [4, 5, 6]])  # 定义一个二维数组
        #
        # a2 = np.mat([[1, 2, 3], [4, 5, 6]])
        #
        # # print(a2.T)
        # #
        # # print(a2.dot(a1))
        #
        # a = np.random.random((3, 4))
        #
        # b = np.random.random((4, 5))
        #
        # print(np.dot(a, b))
        #
        # print(np.matrix(a) * np.matrix(b))
        a1 = np.array([[1,9,53]])
        a2 = np.array([[4,5,6]])
        z = np.array([[3,0,10]])




        axes = plt.subplot(111,projection="3d")
        axes.scatter(a1,a2,z,c='r' , marker="o")

        z = a1*0.2+a2*0.3+0.1

        a1,a2 = np.meshgrid(a1,a2)
        axes.plot_surface(a1,a2,z)
        plt.show()
        import matplotlib.projections

        print(a1,a2)

    def skline(self):

        regression = LinearRegression()
        regression.fit(self.x_data,self.y_data)

        print(regression.predict(self.x_data))

        axes = plt.subplot(1, 1, 1, projection="3d")
        axes.scatter(self.x_data[:, 0], self.x_data[:, 1], self.y_data, c="r", marker="o", s=10)
        x1 = self.x_data[:, 0]
        x2 = self.x_data[:, 1]
        x1, x2 = np.meshgrid(x1, x2)
        z = regression.coef_[0] * x1 +  regression.coef_[1] * x2 + regression.intercept_
        axes.plot_surface(x1, x2, z)
        axes.set_xlabel('Miles')
        axes.set_ylabel('Num of Deliveries')
        axes.set_zlabel('Time')
        plt.show()
        print(regression.coef_[0] ,  regression.coef_[1] ,regression.intercept_)




if __name__ == '__main__':
    mulitRegress=MultiRegression()
    # print(mulitRegress.x_data,mulitRegress.y_data)
    # mulitRegress.skline()
    #
    # mulitRegress.run()
    mulitRegress.polynomialRegression()


