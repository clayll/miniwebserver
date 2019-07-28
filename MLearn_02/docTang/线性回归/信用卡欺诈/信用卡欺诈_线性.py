import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold,cross_val_score,cross_val_predict
from sklearn.metrics import confusion_matrix,recall_score,classification_report
import itertools
from imblearn.over_sampling  import  SMOTE



class CreditCardTest:

    def __init__(self,filePath):
        self.originData = pd.read_csv(filePath)

        self.originX1 = self.originData.loc[:,self.originData.columns !='Class']
        self.originy1 = self.originData.loc[:,self.originData.columns == 'Class']

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

        results_table = pd.DataFrame(columns=['C_parameter', 'Mean recall score','logicModel'])
        results_table['C_parameter'] = c_param_range


        for j,c_param in enumerate(c_param_range,0) :
            recall_accs = []
            reg = LogisticRegression(C=c_param, penalty='l1', solver='liblinear')
            # 分折后的数据
            for train_index, test_index in kf.split(x_train_data):
                # print("TRAIN:", train_index, "TEST:", test_index)


                reg.fit(x_train_data.iloc[train_index], y_train_data.iloc[train_index].values.ravel())
                y_predict = reg.predict(x_train_data.iloc[test_index])

                # 有了预测结果之后就可以来进行评估了，这里recall_score需要传入预测值和真实值。
                recall_acc = recall_score(y_train_data.iloc[test_index].values, y_predict)
                recall_accs.append(recall_acc)

                # 一会还要算平均，所以把每一步的结果都先保存起来。
                # recall_accs.append(recall_acc)

            results_table.iloc[j,1] = np.mean(recall_accs)
            results_table.iloc[j, 2] = reg
        print(results_table)
        # series idxmax() 返回最大值索引
        bset_index = results_table['Mean recall score'].astype('float32').idxmax()

        return results_table.iloc[bset_index,0],results_table.iloc[bset_index,2]

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
                          ,X_test_undersample,y_test_undersample,reg=None,Thresholds = None):
        if reg:

            y_pred_undersample = reg.predict(X_test_undersample.values)
            r1 = classification_report(y_test_undersample, y_pred_undersample)
            # print("r1:",r1)
            cm1 = confusion_matrix(y_test_undersample, y_pred_undersample)

        lr = LogisticRegression(C=best_c, penalty='l1', solver='liblinear')
        lr.fit(X_train_undersample, y_train_undersample.values.ravel())
        y_pred_undersample = lr.predict(X_test_undersample.values)

        if Thresholds:
            y_pred_undersample = lr.predict_proba(X_test_undersample.values)[:,1]>Thresholds

        r2 = classification_report(y_test_undersample, y_pred_undersample)
        cm2 = confusion_matrix(y_test_undersample, y_pred_undersample)
        print("r2:", r2)

        # print("cm1:",cm1)
        # print("cm2:",cm2)
        # 计算所需值
        cnf_matrix = confusion_matrix(y_test_undersample, y_pred_undersample)

        np.set_printoptions(precision=2)

        print("Recall metric in the testing dataset: ", cnf_matrix[1, 1] / (cnf_matrix[1, 0] + cnf_matrix[1, 1]))

        # 绘制
        class_names = [0, 1]
        plt.figure()

        self.plot_confusion_matrix(cnf_matrix,classes=class_names)
        plt.show()


    def diffThresholds(self, best_param_c,X,y,X_test,y_test):
        '''
        不同阈值对结果的影响
        :param best_param_c:
        :param X:
        :param y:
        :param X_test:
        :param y_test:
        :return:
        '''
        reg =  LogisticRegression(C=best_Param_C,penalty="l1",solver="liblinear")

        reg.fit(X,y.values.ravel())
        y_proba = reg.predict_proba(X_test.values)

        j = 1
        # 指定不同的阈值
        thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

        for i in thresholds:
            plt.subplot(3, 3,j)
            y_proba_test = y_proba[:,1] > i

            cnf_matrix = confusion_matrix(y_test, y_proba_test)
            self.plot_confusion_matrix(cnf_matrix,classes= [0, 1],title='thresholds>'+str(i))
            np.set_printoptions(precision=2)

            print("Recall metric in the testing dataset, "+'thresholds> '+str(i)+":  ", cnf_matrix[1, 1] / (cnf_matrix[1, 0] + cnf_matrix[1, 1]))
            j = j + 1

        plt.show()

    def over_sampleS(self,bset_c):

        # 对训练集合测试集进行拆分
        X_train, X_test, y_train, y_test = train_test_split(c.originX1, c.originy1, test_size = 0.2, random_state = 42)

        smote = SMOTE(random_state=0 )

        X_train,y_train = smote.fit_sample(X_train,y_train)

        self.logicRegress_show(bset_c,X_train, pd.DataFrame(y_train),X_test,y_test )



if __name__ == '__main__':
    # c = CreditCardTest(r"C:\文档\ML\第十一章：项目实战-交易数据异常检测\逻辑回归-信用卡欺诈检测\creditcard.csv")

    c = CreditCardTest(r"G:\唐博士\机器学习入门\第十一章：项目实战-交易数据异常检测\逻辑回归-信用卡欺诈检测\creditcard.csv")
    # c.myPrint()

    # c.drawbar(c.originData)
    c.doScale()

    X_undersample, y_undersample = c.undersampl()

    X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = c.dataSplit(X_undersample, y_undersample)

    best_Param_C,reg = c.printing_Kfold_scores(X_train_undersample,y_train_undersample)

    # 下采样的数据去画图，查看情况
    # c.logicRegress_show(best_Param_C,X_train_undersample,y_train_undersample
    #                     ,X_test_undersample,y_test_undersample,reg=reg)

    # 测试三种不同方案的准确率

    #正常的数据,recall值才0.54左右
    X_train, X_test, y_train, y_test = train_test_split(c.originX1, c.originy1, test_size = 0.3, random_state = 42)
    c.logicRegress_show(best_Param_C,X_train,y_train,X_test,y_test)


    # 查看不同阈值的情况
    # c.diffThresholds(best_Param_C,X_train_undersample,y_train_undersample
    #                     ,X_test_undersample,y_test_undersample)
    # 过采样方案的召回率 0.9
    c.over_sampleS(best_Param_C)

    # 采用固定阈值的方案 0.49 最低
    c.logicRegress_show(best_Param_C, X_train, y_train, X_test, y_test,Thresholds=0.5)
