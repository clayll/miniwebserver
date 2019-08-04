from sklearn.datasets import california_housing
from sklearn.model_selection import  train_test_split
from sklearn.tree import  DecisionTreeRegressor
import pydotplus
from sklearn import tree
from IPython.display import Image
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import os
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report,roc_auc_score
import liu_utility

SEED = 42

class DecisionTreeDemo:
    '''
    决策树小案例
    '''
    def __init__(self):
        self.data = california_housing.fetch_california_housing()


        self.X_train, self.X_test, self.y_train, self.y_test =\
            train_test_split(self.data.data,self.data.target,random_state=42,test_size=0.2)


    def getTreeModel(self):
        '''
        创建回归决策树
        :return:回归决策树模型
        '''
        d = DecisionTreeRegressor(max_depth=5)
        d.fit(self.X_train,self.y_train)
        return d

    def showGraph(self,model,filename="dtr_white_background.png"):
        '''
        根据模型展示决策树图
        :param model:
        :return:
        '''
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
        dot_data = tree.export_graphviz(
            model,
            out_file=None,
            feature_names = self.data.feature_names,
            filled=True,
            impurity=False,
            rounded=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        # graph.get_nodes()[7].set_fillcolor("#FFF2DD")
        Image(graph.create_png())
        graph.write_png(filename)

    def getForestModel(self):
        '''
        创建回归的随机森林
        :return:
        '''
        model = RandomForestRegressor(random_state=42,n_estimators=20)
        model.fit(self.X_train, self.y_train)
        return model


    def gridValidate(self,model = None,cv = 5):
        '''
        search 网格交叉验证
        :param model: 随机森林模型
        :param cv:默认5
        :return:暂无
        '''
        tree_param_grid = {'min_samples_split': list((3, 6, 9)), 'n_estimators': list((10, 50, 100))}
        grid = GridSearchCV(model,tree_param_grid,cv)

        # scoring指定损失函数类型，n_jobs指定全部cpu跑，cv指定交叉验证
        grid_result = grid.fit(self.X_train, self.y_train)  # 运行网格搜索
        print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
        # grid_scores_：给出不同参数情况下的评价结果。best_params_：描述了已取得最佳结果的参数的组合
        # best_score_：成员提供优化过程期间观察到的最好的评分
        # 具有键作为列标题和值作为列的dict，可以导入到DataFrame中。
        # 注意，“params”键用于存储所有参数候选项的参数设置列表。
        means = grid_result.cv_results_['mean_test_score']
        params = grid_result.cv_results_['params']
        for mean, param in zip(means, params):
            print("%f  with:   %r" % (mean, param))

class EnsembleStudyDemo:
    '''
    集成学习的demo
    '''
    def __init__(self):
        self.originData = pd.read_csv("input.csv")
        self.y = 1 * (self.originData.cand_pty_affiliation == 'REP')
        self.X_ = self.originData.drop("cand_pty_affiliation",axis=1)
        self.X_ = pd.get_dummies(self.X_,sparse=True)
        self.X_.drop(self.X_.columns[self.X_.std() == 0],axis=1,inplace=True)
        self.X = self.X_
        # 查看结果标签的分布
        # self.originData.cand_pty_affiliation.value_counts(normalize=True).\
        #     plot( kind="bar", title="Share of No. donations")
        # plt.show()

        pd.set_option('display.max_columns', None)


    def getSplitData(self):
        X_train, X_test, y_train, y_test =\
            train_test_split(self.X,self.y,test_size=0.2, random_state=SEED)
        return X_train.values, X_test.values, y_train.values, y_test.values

    def getAllMode(self,X_train, X_test, y_train, y_test):
        nb = liu_utility.getGaussianNB(X_train,y_train)
        svc = liu_utility.getSVC(X_train,y_train,C=10, probability=True)
        knn =liu_utility.getKNeighborsClassifier(X_train,y_train,n_neighbors=3)
        lr = liu_utility.getLogisticRegression(X_train,y_train,C=10, random_state=SEED)
        nn = liu_utility.getMLPClassifier(X_train,y_train,(80, 10), early_stopping=False, random_state=SEED)
        gb = liu_utility.getGradientBoostingClassifier(X_train,y_train,n_estimators=10, random_state=SEED)
        rf = liu_utility.getRandomForestClassifier(X_train,y_train,n_estimators=10, max_features=3, random_state=SEED)
        models = {'svm': svc,
                  'knn': knn,
                  'naive bayes': nb,
                  'mlp-nn': nn,
                  'random forest': rf,
                  'gbm': gb,
                  'logistic': lr,
                  }
        P = np.zeros((y_test.shape[0], len(models)))
        P = pd.DataFrame(P)
        print(P)
        for i,value in models:
            print("算法名称%s:auc的值是：%f" % i,roc_auc_score(y_test, value.predict_proba(X_test)[:, 1]))

if  __name__ == '__main__':
    # 1--测试决策树demo
    # d = DecisionTreeDemo()
    # model  =  d.getTreeModel()
    # # d.showGraph(model)
    # print(model.score(d.X_test, d.y_test))
    # #
    # model1 = d.getForestModel()
    # # print(model1.score(d.X_test, d.y_test))
    #
    # d.gridValidate(model=model1)

    #     2 -- 集成学习demo
    E = EnsembleStudyDemo()
    X_train, X_test, y_train, y_test = E.getSplitData()
    P = np.zeros((y_test.shape[0], 7))
    P = pd.DataFrame(P)
    print(P)
    # m = liu_utility.getDecisionTreeClassifier(X_train,y_train)
    # res = m.predict_proba(X_test)
    # print("roc_auc_score:%f" % roc_auc_score(y_test,res[:,1]))
    #
    # rm = liu_utility.getRandomForestClassifier(X_train,y_train,n_estimators=10,max_depth=3)
    # res1 = rm.predict_proba(X_test)
    # print("roc_auc_score:%f" % roc_auc_score(y_test, res1[:, 1]))
    E.getAllMode(X_train, X_test, y_train, y_test)



