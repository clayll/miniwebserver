import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler



class CreditCardTest:

    def __init__(self,filePath):
        self.originData = pd.read_csv(filePath)


    def myPrint(self):
        print(self.originData.shape)
        print(self.originData.head())

    def drawbar(self,x):

        data = pd.value_counts(x['Class'],sort=True).sort_index()
        print(data)
        data.plot(kind = 'bar')
        plt.title("Fraud class histogram")
        plt.xlabel("Class")
        plt.ylabel("Frequency")
        # plt.show()

    # 对数据做标准化
    def doScale(self):
        y = self.originData['Amount'].values.reshape(-1, 1)
        self.originData['NorAmount'] = StandardScaler().fit_transform(y)
        self.originData = self.originData.drop(['Time','Amount'],axis=1)
        print(self.originData.head())
    # 下采样方案
    def undersampl(self):
        X = self.originData.loc[:,self.originData.columns != 'Class']
        y = self.originData.iloc[:,self.originData.columns == 'Class']

        # 得到所有异常样本的索引
        # 选择表格中的'w'列，使用点属性, 返回的是Series类型
        # dataFrame中的一列来做判断，判断后得到boolean值再将其作为DataFrame的下标过滤DataFrame的数据,True行的数据都被留下来了
        number_records_fraud = len(y[y.Class == 1].index)
        fraud_indices = np.array(y[y.Class == 1].index)

        # 得到所有正常样本的索引
        normal_indices = y[y.Class == 0].index


        np.random.choice()



if __name__ == '__main__':
    c = CreditCardTest(r"C:\文档\ML\第十一章：项目实战-交易数据异常检测\逻辑回归-信用卡欺诈检测\creditcard.csv")
    # c.myPrint()
    # c.drawbar(c.originData)
    c.doScale()

    c.undersampl()