import numpy as np
import matplotlib.pyplot as plt
from sklearn import  preprocessing
from sklearn import linear_model



class PolynomialLogicRegression():
    def __init__(self):
        data = np.genfromtxt("./datas/LR-testSet2.txt", delimiter=",")
        self.x = data[:, 0:2]
        self.y = data[:, -1, np.newaxis]
        self.m = len(self.y)
        self.epoch = 10000
        self.ws = np.ones((3,1))
        self.lr = 0.01
        self.model = preprocessing.PolynomialFeatures(degree=3)

    # sigmoid，x大于0，则分类算1
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def caculateLoss(self,ws,x_data):

        left = np.multiply(-self.y,np.log(x_data*ws))
        right = np.multiply(-(1-self.y)*np.log(1-x_data*ws))
        return  np.sum(left + right)/self.m

    def showPlotSource(self,ws):
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

        # 取得最大值以及最小值

        x_min, x_max = self.x[:,0].min()-1, self.x[:,0].max()+1
        y_min, y_max = self.x[:,1].min() - 1, self.x[:,1].max() + 1

        xx = np.arange(x_min, x_max, 0.02)
        yy = np.arange(y_min, y_max, 0.02)

        xx,yy = np.meshgrid(xx,yy)


        zz = np.c_[xx.ravel(),yy.ravel()]
        print(zz.shape,ws.shape)

        zz = self.model.fit_transform(zz).dot(ws)

        zz = self.sigmoid(zz)

        for i in range(len(zz)):
            if zz[i,0] > 0.5:
                zz[i, 0] = 1
            else:
                zz[i, 0] = 0


        print(zz.shape,xx.shape,yy.shape)
        zz = zz.reshape(xx.shape)
        plt.contourf(xx,yy,zz)

        plt.show()

    def showPlot2(self):
        pass

    def prepareData(self):

        x_mat= self.model.fit_transform(self.x)

        ws = np.ones((x_mat.shape[1],1))
        for i in range(self.epoch):
            # xMat和weights矩阵相乘
            h = self.sigmoid(np.dot(x_mat, ws))

            # 计算误差
            ws_grad = np.dot(x_mat.T , (h - self.y)) / self.m

            ws = ws - self.lr * ws_grad

        return ws

    def test(self):

        pp = preprocessing.PolynomialFeatures()
        x = np.array([2, 3]).reshape(1, 2)
        y = np.array([4, 5]).reshape(1, 2)

        # x1 = pp.fit_transform(x,y)
        print(pp.fit_transform(x, y))
        # print(y1)

    def skcaculate(self):
        x_data = self.model.fit_transform(self.x)
        line = linear_model.LogisticRegression()
        line.fit(x_data,self.y)
        print(line.coef_,line.intercept_)
        return line.coef_, line.predict(x_data)


if __name__ == '__main__':
    poloynomial = PolynomialLogicRegression()

    # ws = poloynomial.prepareData()
    # print(ws)
    # poloynomial.showPlotSource(ws)

    ws = poloynomial.skcaculate()
    poloynomial.showPlotSource(ws.reshape(10,1))


