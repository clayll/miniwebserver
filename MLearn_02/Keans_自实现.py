import numpy as np
import matplotlib.pyplot as plt

class KmeansRealization():
    def __init__(self):
        self.data = np.genfromtxt("./datas/kmeans.txt", delimiter=" ")
        self.x_data = self.data[:,0]
        self.y_data = self.data[:,1]

    # 初始化出质心
    def init_K(self, k):
        indexs = np.random.randint(0,len(self.data)-1,(4,1))
        centroids = self.data[indexs.ravel().tolist()]
        return centroids

    # 计算亮点之间的距离
    def getDistance(self,data1,data2):

        distince = (data1-data2)**2
        return np.sqrt((distince).sum())




    def myPlt(self):
        plt.scatter(self.x_data,self.y_data)


if __name__ == '__main__':
    kmeansRealization = KmeansRealization()
    kmeansRealization.init_K(4)
    print(kmeansRealization.getDistance(np.array([1.0,3.0],dtype=np.float),np.array([5.0,6.0],dtype=np.float)))
    kmeansRealization.myPlt()