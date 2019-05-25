from sklearn import tree
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np


class TreeNoneLine():
    def __init__(self):
        self.data = np.genfromtxt("./datas/LR-testSet2.txt",delimiter=",")
        self.x_data = self.data[:,:-1]
        self.y_data = self.data[:,-1:]
        self.X_train, self.X_test, self.y_train, self.y_test \
            = train_test_split(self.x_data,self.y_data)




    def plt(self,model):

        plt.scatter(self.x_data[:,0],self.x_data[:,1],c=self.y_data.ravel())

        # 等高线图
        xmin,xmax = self.x_data[:,0].min()-1,self.x_data[:,0].max()+1
        ymin,ymax = self.x_data[:,1].min()-1,self.x_data[:,1].max()+1

        x_data = np.arange(xmin,xmax,0.02)
        y_data = np.arange(ymin,ymax,0.02)

        # 生成网格
        xx,yy = np.meshgrid(x_data,y_data)
        # 生成网格的点，x和y结合成一个坐标点
        zz = np.c_[xx.ravel(),yy.ravel()]
        zz = model.predict(zz)
        plt.contourf(xx,yy,zz.reshape(xx.shape),alpha=0.8)
        # plt.show()

    def treeMode(self):
        treeClassifier = tree.DecisionTreeClassifier(max_depth=7,min_samples_split=3)
        treeClassifier.fit(self.X_train,self.y_train)
        print(treeClassifier.score(self.X_test,self.y_test))
        return treeClassifier

    def knnMode(self):
        knnClassifer = neighbors.KNeighborsClassifier()
        knnClassifer.fit(self.X_train,self.y_train.ravel())
        print(knnClassifer.score(self.X_test, self.y_test))
        return knnClassifer

    def RandomForestMode(self):
        randomForest = RandomForestClassifier(n_estimators=100)
        randomForest.fit(self.X_train,self.y_train.ravel())
        print(randomForest.score(self.X_test, self.y_test))
        return randomForest


if __name__ == '__main__':

    treeNoneLine = TreeNoneLine()
    knnMode = treeNoneLine.knnMode()
    treeMode = treeNoneLine.treeMode()
    randomForestMode = treeNoneLine.RandomForestMode()
    treeNoneLine.plt(randomForestMode)

    plt.show()
    # x = np.array([1,2,3])
    # y = np.array([4,5,6])
    # xx,yy = np.meshgrid(x,y)
    # zz = np.c_[xx.ravel(),yy.ravel()]

