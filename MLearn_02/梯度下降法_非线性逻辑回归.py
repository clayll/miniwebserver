import numpy as np
import matplotlib.pyplot as plt
from sklearn import  preprocessing


class PolynomialLogicRegression():
    def __init__(self):
        data = np.genfromtxt("./datas/LR-testSet2.txt", delimiter=",")
        self.x = data[:, 0:2]
        self.y = data[:, -1, np.newaxis]
        self.m = len(self.y)

    # sigmoid，x大于0，则分类算1
    def sigmoid(self,x):

        return 1/(1+np.exp(-x))

    def caculateLoss(self,ws,x_data):
        left = 0
        right = 0
        left = -np.log(x_data*ws)
        right = -np.log(1-x_data*ws)

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
        x = np.array([[1,2],[2,3]])
        print(model.fit_transform(x))



if __name__ == '__main__':
    poloynomial = PolynomialLogicRegression()
    poloynomial.prepareData()