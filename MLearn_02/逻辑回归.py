import numpy as np
import matplotlib.pyplot as plt


class LogicRegression():
    def __init__(self):
        data = np.genfromtxt("./datas/LR-testSet.csv", delimiter=",")
        self.x = data[:,0:2]
        self.y = data[:,-1,np.newaxis]

        self.count = 10000
        self.w1,self.w2,self.b = 0,0,0



    def sigmoid(self,w1,w2,b):

        ws = b+w1*self.x[:,0] + w2*self.x[:,1]

        return 1/(np.log(-ws)+1)

    def lossDerivatives(self):
        x_data = np.concatenate((np.ones(len(self.y),1),self.x),axis=1)

        for i in range(self.count+1):
            ws = self.sigmoid()
            for i in len(self.y):
                pass





    def run(self):
        plt.plot(self.x[:,0],self.x[:,1],'cx')
        plt.plot(self.x[:,1],self.x[:,0],'ro')

        plt.show()


if __name__ == '__main__':
    logicRegress =    LogicRegression()
    # print(logicRegress.x)
    # print(logicRegress.y)
    print(logicRegress.x[0].shape)
    logicRegress.run()