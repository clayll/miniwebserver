from sklearn import tree
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
# from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np


class TreeLineModel():

    def __init__(self):
        self.data = np.genfromtxt("./datas/LR-testSet.csv",delimiter=",")
        self.x_data = self.data[:,0:-1]
        self.y_data = self.data[:,-1:]

        # self.x_train, self.X_test, self.y_train, self.y_test = train_test_split(
        #     self.x_data, self.y_data, test_size = 0.25)

    def plot(self,model):
        x0,y0,x1,y1 = [],[],[],[]
        for i in range(len(self.y_data)):
            if self.y_data[i,0] == 0:
                x0.append(self.x_data[i,0])
                y0.append(self.x_data[i,1])
            else:
                x1.append(self.x_data[i,0])
                y1.append(self.x_data[i,1])
        plt.plot(np.array(x0)[:,np.newaxis],np.array(y0)[:,np.newaxis],"b.")
        plt.plot(np.array(x1)[:,np.newaxis],np.array(y1)[:,np.newaxis],"c.")


        # 等高图
        xmin,ymin = self.x_data[:,0].min()-1,self.x_data[:,1].min()-1
        xmax,ymax =self.x_data[:,0].max()+1,self.x_data[:,1].max()+1
        x_data,y_data = np.meshgrid(np.arange(xmin,xmax,0.02),np.arange(ymin,ymax,0.02))

        zz = np.c_[np.ravel(x_data),np.ravel(y_data)]

        y_predict = model.predict(zz)
        plt.contourf(x_data,y_data,y_predict.reshape(x_data.shape))
        plt.show()

    def modelProduce(self, type="tree"):
        if type == 'tree':
            treeMode = tree.DecisionTreeClassifier()
            treeMode.fit(self.x_data,self.y_data)

            return treeMode
        else:
            lineRegression = LinearRegression()
            lineRegression.fit(self.x_data,self.y_data)
            return lineRegression

    def linePlot(self,model):

        plt.scatter(self.x_data[:,0],self.x_data[:,1],c=self.y_data.ravel())

        model.predict([[]])
        plt.show()

if __name__ == '__main__':
    treeLine = TreeLineModel()
    treeMode = treeLine.modelProduce()
    lineMode = treeLine.modelProduce(type="line")

    treeLine.linePlot(lineMode)
    # treeLine.plot(treeMode)
    # print(classification_report(treeLine.y_data,treeMode.predict(treeLine.x_data)))
