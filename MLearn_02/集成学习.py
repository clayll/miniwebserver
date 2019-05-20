from sklearn import neighbors
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier

import matplotlib.pyplot as plt

import numpy as np

def polt(x_data,y_data,type=""):
    pass

class bagging():
    def __init__(self):
        self.data = np.genfromtxt("./datas/LR-testSet2.txt",delimiter=",")
        self.x_data = self.data[:,0:-1]
        self.y_data = self.data[:,-1:]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.x_data,  self.y_data)

    def knnModel(self):
        knn = neighbors.KNeighborsClassifier()
        knn.fit(self.X_train,self.y_train)
        print(knn.score(self.X_test,self.y_test))
        return knn

    def treeMode(self):
        treemode = tree.DecisionTreeClassifier()
        treemode.fit(self.X_train,self.y_train)
        print(treemode.score(self.X_test,self.y_test))
        return treemode

    def baggingMode(self,mode):
        bag = BaggingClassifier(mode)
        bag.fit(self.X_train, self.y_train)
        print(bag.score(self.X_test, self.y_test))

if __name__ == '__main__':
    bag = bagging()
    bag.baggingMode(bag.knnModel())
    bag.baggingMode(bag.treeMode())
