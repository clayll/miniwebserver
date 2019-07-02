import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GradientTest():
    def __init__(self):
        self.data = ""


    # 导入数据
    def importData(self):
        self.data = pd.read_csv("./data/LogiReg_data.txt",names=['Exam 1', 'Exam 2', 'Admitted'])
        self.y = ""

    def drawScatter(self):

        positive = self.data[self.data[
                              'Admitted'] == 1]  # returns the subset of rows such Admitted = 1, i.e. the set of *positive* examples
        negative = self.data[
            self.data['Admitted'] == 0]  # returns the subset of rows such Admitted = 0, i.e. the set of *negative* exampl
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.scatter(positive['Exam 1'], positive['Exam 2'], s=30, c='b', marker='o', label='Admitted')
        ax.scatter(negative['Exam 1'], negative['Exam 2'], s=30, c='r', marker='x', label='Not Admitted')
        ax.legend()
        ax.set_xlabel('Exam 1 Score')
        ax.set_ylabel('Exam 2 Score')
        plt.show()

    # 定义sigmode函数
    def sigmoid(self,z):
        return 1 / (1 + np.exp(-z))

    #建立模型
    def model(self,X, theta):
        return self.sigmoid(np.dot(X, theta.T))

if __name__ == '__main__':
    g = GradientTest()
    g.importData()
    g.drawScatter()