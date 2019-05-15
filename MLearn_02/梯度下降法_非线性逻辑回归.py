import numpy as np
import matplotlib.pyplot as plt
from sklearn import  preprocessing


class PolynomialLogicRegression():
    def __init__(self):
        data = np.genfromtxt("./datas/LR-testSet2.txt", delimiter=",")
        self.x = data[:, 0:2]
        self.y = data[:, -1, np.newaxis]
        self.m = len(self.y)
        self.epoch = 10000
        self.ws = np.ones((3,1))
        self.lr = 0.01

    # sigmoid，x大于0，则分类算1
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def caculateLoss(self,ws,x_data):

        left = np.multiply(-self.y,np.log(x_data*ws))
        right = np.multiply(-(1-self.y)*np.log(1-x_data*ws))
        return  np.sum(left + right)/self.m

    def showPlotSource(self):
        x0,y0,x1,y1 = [],[],[],[]
        for i in range(self.m):
            if self.y[i,0] == 0:
                x0.append(self.x[i,0])
                y0.append(self.x[i,1])
            else:
                x1.append(self.x[i, 0])
                y1.append(self.x[i, 1])

        plt.plot(x0,y0,'co')
        plt.plot(x1,y1,'rx')
        plt.show()

    def prepareData(self):
        model = preprocessing.PolynomialFeatures()
        x_mat= model.fit_transform(self.x)

        ws = np.ones((x_mat.shape[1],1))
        for i in range(self.epoch):
            # xMat和weights矩阵相乘
            h = self.sigmoid(np.dot(x_mat, ws))

            # 计算误差
            ws_grad = np.dot(x_mat.T , (h - self.y)) / self.m

            ws = ws - self.lr * ws_grad

        return ws


if __name__ == '__main__':
    poloynomial = PolynomialLogicRegression()
    print(poloynomial.prepareData())

