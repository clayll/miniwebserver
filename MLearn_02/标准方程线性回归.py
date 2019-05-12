import numpy as np
import matplotlib.pyplot as plt


'''实现线性回归方程'''
class NormalRegression():
    def __init__(self):
        data = np.genfromtxt("./datas/data.csv",delimiter=',')
        self.x_data = data[:,0,np.newaxis]
        self.y_data = data[:,1, np.newaxis]

        self.w0 = 0
        self.w1 = 0


    def model(self):
        # axis 1 表示是行  axis 0 表示是列
        z = np.ones((100,1),dtype=np.float)

        x = np.concatenate((z,self.x_data),axis=1)
        x = np.mat(x)
        y = np.mat(self.y_data)
        xTx = (x.T*x)
        # 计算矩阵的行列式值，如果为0，说明没有逆矩阵 根据逆矩阵的公式：该矩阵的值不能为0
        if  np.linalg.det(xTx) == 0.0:
            print("没有逆矩阵")
            return

        z = xTx.I*x.T*y
        return z


    def run(self):
        plt.plot(self.x_data,self.y_data,"c.")
        x_test = [[15],[34],[79]]
        ws = self.model()
        print(ws)
        y_test = x_test*ws[1]+ws[0]
        plt.plot(x_test,y_test,c='r')
        plt.show()

if __name__ == '__main__':
    normal = NormalRegression()
    normal.run()