import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import RidgeCV
from sklearn import linear_model

class RidgeRegression():
    def __init__(self):
        data = np.genfromtxt("./datas/longley.csv",delimiter=",")
        self.x = data[1:,2:]
        self.y = data[1:,1]



    def runSK(self):
        alphas_test = np.linspace(0.001,1,50)

        ridge = RidgeCV(alphas=alphas_test ,store_cv_values=True)
        ridge.fit(self.x,self.y)

        print(ridge.intercept_)
        print(ridge.coef_)
        print(ridge.alpha_)

        print(ridge.predict(self.x[2,np.newaxis]))


        plt.plot(alphas_test,ridge.cv_values_.mean(axis=0),'c')
        plt.plot(ridge.alpha_,min(ridge.cv_values_.mean(axis=0)),'ro')
        plt.show()


    def runRige(self,alambda=0.2):
        x = np.mat( np.concatenate(( np.ones(self.y.shape)[:,np.newaxis],self.x),axis=1))
        y = np.mat(self.y[:,np.newaxis])

        xTx=x.T*x+alambda*np.mat(np.ones(x.shape[1]))

        # 逆矩阵不能为空
        if np.linalg.det(xTx) == 0.0:
            print("逆矩阵不能为0")
            return

        ws=(xTx.I)*x.T*y
        print(ws)

        print(self.y)
        print(x*np.mat(ws))

    
    def runLasso(self):
        lasso = linear_model.LassoCV()
        lasso.fit(self.x,self.y)
        print(self.y)
        print(lasso.coef_,lasso.intercept_,lasso.alpha_,lasso.predict(self.x[0:4]))


    # 弹性网
    def runNet(self):
        net = linear_model.ElasticNetCV()
        net.fit(self.x,self.y)
        print(net.coef_, net.intercept_, net.alpha_, net.predict(self.x[0:4]))





if __name__ == '__main__':
    ridge = RidgeRegression()
    # ridge.runRige()
    ridge.runLasso()
    print("*"*40)
    ridge.runNet()
