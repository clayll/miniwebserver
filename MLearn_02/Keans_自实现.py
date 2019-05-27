import numpy as np
import matplotlib.pyplot as plt

class KmeansRealization():
    def __init__(self):
        self.data = np.genfromtxt("./datas/kmeans.txt", delimiter=" ")
        self.x_data = self.data[:,0]
        self.y_data = self.data[:,1]
        self.k = 4

    # 初始化出质心
    def init_K(self, k):
        indexs = np.random.randint(0,len(self.data)-1,(k,1))
        centroids = self.data[indexs.ravel().tolist()]
        return centroids

    # 计算亮点之间的距离
    def getDistance(self,data1,data2):
        distince = (data1-data2)**2
        return np.sqrt((distince).sum())

    def reCaculateCentroid(self,beforeCentroids: np.ndarray):
        # beforeCentroids.su
        pass

    def caculateCentroid(self):
        miniDistance, listCentroid= 10000,[]
        centroids = self.init_K(self.k)
        for i in range(self.k):
            centroid = centroids[i]
            for j in range(len(self.x_data)):
                distnce = self.getDistance(centroid, self.data[j])
                if distnce < miniDistance:
                    miniDistance = distnce

                listCentroid.append(i,self.data[j])


    def myPlt(self):
        plt.scatter(self.x_data,self.y_data)


if __name__ == '__main__':
    kmeansRealization = KmeansRealization()
    s = kmeansRealization.init_K(4)

    a = np.array([[1,[1,2]],[2,[3,4]]])

    # b = np.array([[2, 2], [3, 4]])
    # print((a == b).all())
    # print(kmeansRealization.getDistance(np.array([1.0,3.0],dtype=np.float),np.array([5.0,6.0],dtype=np.float)))
    # kmeansRealization.myPlt()