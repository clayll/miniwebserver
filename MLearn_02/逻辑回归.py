import numpy as np
import matplotlib.pyplot as plt
from sklearn import  preprocessing
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

# 自定义逻辑回归
class LogicRegression():
    def __init__(self):
        data = np.genfromtxt("./datas/LR-testSet.csv", delimiter=",")
        self.x = data[:,0:2]
        self.y = data[:,-1,np.newaxis]

        self.count = 10000

        self.loss=[]

        self.m = len(self.y)
        self.lr = 0.001
        self.scale = True

        if self.scale:
            self.x = preprocessing.scale(self.x)
            print(type(self.x))

    # 逻辑回归函数，其中x为线性回归公式
    def sigmoid(self,x):

        # 算e的x次幂
        return 1/(np.exp(-x)+1)

    # 计算损失数
    def caculateLoss(self,ws,x_data):

        left = np.multiply(-self.y,(np.log(self.sigmoid(x_data*ws))))

        right = np.multiply(-(1-self.y),np.log(1-self.sigmoid(x_data*ws)))

        return  np.sum(left+right)/self.m

    # 梯度下降函数
    def lossDerivatives(self):

        x_data = np.concatenate((np.ones( (self.m, 1)), self.x), axis=1)

        x_mat = np.mat(x_data)

        y_mat = np.mat(self.y)
        ws = np.mat(np.ones( (x_mat.shape[1],1)))

        for i in range(self.count+1):
            # xMat和weights矩阵相乘
            h = self.sigmoid(x_mat * ws)
            # 计算误差
            ws_grad = x_mat.T * (h - y_mat) / self.m

            ws = ws - self.lr * ws_grad

            if i % 50 == 0:

                self.loss.append(self.caculateLoss(ws,x_mat))
        return ws

    # 显示数据
    def showPlot(self,ws):
        x0,y0,x1,y1 = [],[],[],[]
        for i in range(self.m ):
            if self.y[i,0] == 0:
                x0.append(self.x[i,0])
                y0.append(self.x[i,1])
            else:
                x1.append(self.x[i, 0])
                y1.append(self.x[i, 1])

        ws = np.array(ws.tolist())
        plt.plot(x0, y0, 'cx')
        plt.plot(x1, y1, 'ro')
        x_test = [[-4], [3]]
        y_test = (-ws[0] - x_test * ws[1]) / ws[2]
        plt.plot(x_test ,y_test ,'k')
        plt.show()

    # 显示代价图
    def showLossPlot(self):
        x_data = np.linspace(1,len(self.loss)+1,num=len(self.loss))

        plt.plot(x_data,self.loss,'c')
        plt.show()


    # 显示报告
    def showReport(self, ws):
        x_data = np.concatenate((np.ones((self.m, 1)), self.x), axis=1)

        x_mat = np.mat(x_data)

        y_test = [1 if x > 0.5 else 0 for x in self.sigmoid(x_mat*ws)]

        print(classification_report(self.y,y_test))

    def skCacatulate(self):
        line = LogisticRegression()
        line.fit(self.x,self.y)
        y_result = line.predict(self.x)



        print(classification_report(self.y,y_result))

if __name__ == '__main__':
    logicRegress =    LogicRegression()

    # print(logicRegress.x)
    # print(logicRegress.y)
    # # print(logicRegress.y.shape)
    # ws = logicRegress.lossDerivatives()
    #
    # logicRegress.showPlot(ws)
    # logicRegress.showLossPlot()
    # logicRegress.showReport(ws)

    logicRegress.skCacatulate()
