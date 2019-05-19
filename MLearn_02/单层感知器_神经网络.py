import numpy as np
import matplotlib.pyplot as plt

class Perceptron():
    def __init__(self):
        self.t = np.array([1,1,-1,-1]).reshape((4,1))
        self.x_data =  np.array([[1,3,3],[1,4,3],[1,1,1],[1,0,2]])
        self.lr = 0.11
        self.ws  = (np.random.random([3,1])-0.5)*2

    def update(self):
        y = np.sign( np.dot(self.x_data, self.ws))
        self.ws = self.ws + np.dot(self.x_data.T, ((self.t - y)*self.lr)) / self.x_data.shape[0]
        return y

    def run(self):
        for i in range(100):
            y = self.update()
            if (self.t == y).all():
                print('epoch:', i)
                print(self.ws)
                break

    def showPlt(self):
        plt.plot(self.x_data[0:2,1],self.x_data[0:2,2],'co')
        plt.plot(self.x_data[2:4,1], self.x_data[2:4,2], 'ro')
        print(self.ws)
        # plt.plot(self.x_data[:,1], np.dot(self.x_data,self.ws),"kx")
        k = -self.ws[1]/self.ws[2]
        b = -self.ws[0]/self.ws[2]
        plt.plot(self.x_data[:,1],self.x_data[:,1]*k+b,'k')
        plt.show()

    def prodict(self):
        return

if __name__ == '__main__':
    p = Perceptron()
    p.run()
    p.showPlt()