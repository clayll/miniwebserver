import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold,cross_val_score,cross_val_predict
from sklearn.metrics import confusion_matrix,recall_score,classification_report
import itertools




class CreditCardTest:

    def __init__(self,filePath):
        self.originData = pd.read_csv(filePath)

        self.originX = self.originData.loc[:,self.originData.columns !='Class']
        self.originX = self.originData.loc[:,self.originData.columns == 'Class']

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
        self.originX = self.originData.loc[:, self.originData.columns != 'Class']
        self.originy = self.originData.loc[:, self.originData.columns == 'Class']


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
        random_normal_indices = np.random.choice(normal_indices,number_records_fraud,replace=False)

        # 有了正常和异常样本后把它们的索引都拿到手

        under_sample_indices = np.concatenate((fraud_indices, random_normal_indices))

        # 根据索引得到下采样所有样本点
        under_sample_data = self.originData.iloc[under_sample_indices, :]

        X_undersample = under_sample_data.loc[:,under_sample_data.columns!='Class']
        y_undersample = under_sample_data.loc[:, under_sample_data.columns == 'Class']

        # 下采样 样本比例
        print("Percentage of normal transactions: ",
              len(under_sample_data[y_undersample.Class == 0]) / len(under_sample_data))
        print("Percentage of fraud transactions: ",
              len(under_sample_data[y_undersample.Class == 1]) / len(under_sample_data))
        print("Total number of transactions in resampled data: ", len(under_sample_data))

        return  X_undersample,y_undersample

    # 数据集的划分,X,y为采样的变量数据
    def dataSplit(self,X,y):
        X_train, X_test, y_train, y_test = train_test_split(
        self.originX, self.originy, test_size = 0.3, random_state = 42)

        print("Number transactions train dataset: ", len(X_train))
        print("Number transactions test dataset: ", len(X_test))
        print("Total number of transactions: ", len(X_train) + len(X_test))

        X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = train_test_split(
            X, y, test_size=0.3, random_state=42)

        print("")
        print("Number transactions train dataset: ", len(X_train_undersample))
        print("Number transactions test dataset: ", len(X_test_undersample))
        print("Total number of transactions: ", len(X_train_undersample) + len(X_test_undersample))

        return X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample

    # 根据不用的正则化惩罚项目，交叉验证,选择出最好的惩罚参数
    def printing_Kfold_scores(self,x_train_data, y_train_data):
        kf = KFold(n_splits=5,shuffle=True)

        # 定义不同力度的正则化惩罚力度
        c_param_range = [0.01, 0.1, 1, 10, 100]

        results_table = pd.DataFrame(columns=['C_parameter', 'Mean recall score'])
        results_table['C_parameter'] = c_param_range


        for j,c_param in enumerate(c_param_range,0) :
            recall_accs = []
            # 分折后的数据
            for train_index, test_index in kf.split(x_train_data):
                # print("TRAIN:", train_index, "TEST:", test_index)

                reg = LogisticRegression(C = c_param, penalty = 'l1',solver='liblinear')
                reg.fit(x_train_data.iloc[train_index], y_train_data.iloc[train_index].values.ravel())
                y_predict = reg.predict(x_train_data.iloc[test_index])

                # 有了预测结果之后就可以来进行评估了，这里recall_score需要传入预测值和真实值。
                recall_acc = recall_score(y_train_data.iloc[test_index].values, y_predict)
                recall_accs.append(recall_acc)

                # 一会还要算平均，所以把每一步的结果都先保存起来。
                # recall_accs.append(recall_acc)

            results_table.iloc[j,1] = np.mean(recall_accs)
        print(results_table)
        # series idxmax() 返回最大值索引
        return results_table.iloc[results_table['Mean recall score'].astype('float32').idxmax(),0]

    # 画图，混淆矩阵
    def plot_confusion_matrix(self,cm, classes,
                              title='Confusion matrix',
                              cmap=plt.cm.Blues):
        """
        绘制混淆矩阵
        """

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=0)
        plt.yticks(tick_marks, classes)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    def logicRegress_show(self,best_c,X_train_undersample,y_train_undersample
                          ,X_test_undersample,y_test_undersample):
        lr = LogisticRegression(C=best_c, penalty='l1',solver='liblinear')
        lr.fit(X_train_undersample, y_train_undersample.values.ravel())
        y_pred_undersample = lr.predict(X_test_undersample.values)

        # 计算所需值
        cnf_matrix = confusion_matrix(y_test_undersample, y_pred_undersample)
        print(cnf_matrix)
        np.set_printoptions(precision=2)

        print("Recall metric in the testing dataset: ", cnf_matrix[1, 1] / (cnf_matrix[1, 0] + cnf_matrix[1, 1]))

        # 绘制
        class_names = [0, 1]
        plt.figure()
        print(type(cnf_matrix))
        self.plot_confusion_matrix(cnf_matrix,classes=class_names)
        plt.show()


if __name__ == '__main__':
    c = CreditCardTest(r"C:\文档\ML\第十一章：项目实战-交易数据异常检测\逻辑回归-信用卡欺诈检测\creditcard.csv")
    # c.myPrint()
    # c.drawbar(c.originData)
    c.doScale()

    X_undersample, y_undersample = c.undersampl()

    X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = c.dataSplit(X_undersample, y_undersample)

    best_Param_C = c.printing_Kfold_scores(X_train_undersample,y_train_undersample)

    c.logicRegress_show(best_Param_C,X_train_undersample,y_train_undersample
                        ,X_test_undersample,y_test_undersample)

