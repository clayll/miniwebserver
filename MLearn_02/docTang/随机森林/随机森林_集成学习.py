from sklearn.datasets import california_housing
from sklearn.model_selection import  train_test_split,KFold
from sklearn.tree import  DecisionTreeRegressor
import pydotplus
from sklearn import tree
from IPython.display import Image
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor,GradientBoostingClassifier
from mlens.ensemble import SuperLearner
import os
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report,roc_auc_score
import liu_utility
from mlens.visualization import corrmat
import matplotlib.pyplot   as plt
from sklearn.metrics import roc_curve
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.kernel_approximation import Nystroem
from sklearn.kernel_approximation import RBFSampler
from sklearn.pipeline import make_pipeline
from sklearn.base import clone



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
            train_test_split(self.X,self.y,test_size=0.9, random_state=SEED)
        return X_train.values, X_test.values, y_train.values, y_test.values

    def getAllMode(self,X_train, X_test, y_train, y_test):
        nb = liu_utility.getGaussianNB(X_train,y_train)
        svc = liu_utility.getSVC(X_train,y_train,C=10, probability=True)
        knn =liu_utility.getKNeighborsClassifier(X_train,y_train,n_neighbors=3)
        lr = liu_utility.getLogisticRegression(X_train,y_train,C=10, random_state=SEED)
        nn = liu_utility.getMLPClassifier(X_train,y_train,(80, 10),random_state=SEED)
        gb = liu_utility.getGradientBoostingClassifier(X_train,y_train,n_estimators=10, random_state=SEED)
        rf = liu_utility.getRandomForestClassifier(X_train,y_train,n_estimators=10, max_depth=3, random_state=SEED)
        models = {'svm': svc,
                  'knn': knn,
                  'naive bayes': nb,
                  'mlp-nn': nn,
                  'random forest': rf,
                  'gbm': gb,
                  'logistic': lr,
                  }
        return models
        # P = np.zeros((y_test.shape[0], len(models)))
        # P = pd.DataFrame(P)
        # columns=[]
        # for i,(name,item) in enumerate(models.items(),start=0) :
        #     P.iloc[:,i] = item.predict_proba(X_test)[:, 1]
        #     columns.append(name)
        #     print("算法名称{0}:auc的值是：{1}".format(name,roc_auc_score(y_test, P.iloc[:,i])))
        #
        # P.columns= columns
        # return P

        print("Ensemble ROC-AUC score: %.3f" % roc_auc_score(y_test, P.mean(axis=1)))
        # corrmat(P.corr(),inflate=False)
        # plt.show()

    def train_predict(self,model_list,X_train, X_test, y_train):
        """Fit models in list on training set and return preds"""
        P = np.zeros((y_test.shape[0], len(model_list)))
        P = pd.DataFrame(P)

        print("Fitting models.")
        cols = list()
        for i, (name, m) in enumerate(model_list.items()):
            print("%s..." % name, end=" ", flush=False)
            m.fit(X_train, y_train)
            P.iloc[:, i] = m.predict_proba(X_test)[:, 1]
            cols.append(name)
            print("done")

        P.columns = cols
        print("Done.\n")
        return P

    def score_models(self,P, y):
        """Score model in prediction DF"""
        print("Scoring models.")
        for m in P.columns:
            score = roc_auc_score(y, P.loc[:, m])
            print("%-26s: %.3f" % (m, score))
        print("Ensemble ROC-AUC score: %.3f" % roc_auc_score(y, P.mean(axis=1)))

    def plot_roc_curve(self,ytest, P_base_learners, P_ensemble, labels, ens_label):
        """Plot the roc curve for base learners and ensemble."""
        plt.figure(figsize=(10, 8))
        plt.plot([0, 1], [0, 1], 'k--')

        cm = [plt.cm.rainbow(i)
              for i in np.linspace(0, 1.0, P_base_learners.shape[1] + 1)]

        for i in range(P_base_learners.shape[1]):
            p = P_base_learners[:, i]
            fpr, tpr, _ = roc_curve(ytest, p)
            plt.plot(fpr, tpr, label=labels[i], c=cm[i + 1])

        fpr, tpr, _ = roc_curve(ytest, P_ensemble)
        plt.plot(fpr, tpr, label=ens_label, c=cm[0])

        plt.xlabel('False positive rate')
        plt.ylabel('True positive rate')
        plt.title('ROC curve')
        plt.legend(frameon=False)
        plt.show()

    def train_base_learners(self,base_learners, inp, out, verbose=True):
        """Train all base learners in the library."""
        if verbose: print("Fitting models.")
        for i, (name, m) in enumerate(base_learners.items()):
            if verbose: print("%s..." % name, end=" ", flush=False)
            m.fit(inp, out)
            if verbose: print("done")

    def predict_base_learners(self,pred_base_learners, inp, verbose=True):
        """Generate a prediction matrix."""
        P = np.zeros((inp.shape[0], len(pred_base_learners)))

        if verbose: print("Generating base learner predictions.")
        for i, (name, m) in enumerate(pred_base_learners.items()):
            if verbose: print("%s..." % name, end=" ", flush=False)
            p = m.predict_proba(inp)
            # With two classes, need only predictions for one class
            P[:, i] = p[:, 1]
            if verbose: print("done")

        return P

    def ensemble_predict(self,base_learners, meta_learner, inp, verbose=True):
        """Generate predictions from the ensemble."""
        P_pred = self.predict_base_learners(base_learners, inp, verbose=verbose)
        return P_pred, meta_learner.predict_proba(P_pred)[:, 1]

    def get_models(self):
        """Generate a library of base learners."""
        nb = GaussianNB()
        svc = SVC(C=100, probability=True)
        knn = KNeighborsClassifier(n_neighbors=3)
        lr = LogisticRegression(C=100, random_state=SEED)
        nn = MLPClassifier((80, 10), early_stopping=False, random_state=SEED)
        gb = GradientBoostingClassifier(n_estimators=100, random_state=SEED)
        rf = RandomForestClassifier(n_estimators=10, max_features=3, random_state=SEED)

        models = {'svm': svc,
                  'knn': knn,
                  'naive bayes': nb,
                  'mlp-nn': nn,
                  'random forest': rf,
                  'gbm': gb,
                  'logistic': lr,
                  }

        return models

    def stacking(self,base_learners, meta_learner, X, y, generator):
        """Simple training routine for stacking."""

        # Train final base learners for test time
        print("Fitting final base learners...", end="")
        self.train_base_learners(base_learners, X, y, verbose=False)
        print("done")

        # Generate predictions for training meta learners
        # Outer loop:
        print("Generating cross-validated predictions...")
        cv_preds, cv_y = [], []
        for i, (train_idx, test_idx) in enumerate(generator.split(X)):
            fold_xtrain, fold_ytrain = X[train_idx, :], y[train_idx]
            fold_xtest, fold_ytest = X[test_idx, :], y[test_idx]

            # Inner loop: step 4 and 5
            # 克隆这个对象，避免同样的对象呗训练
            fold_base_learners = {name: clone(model)
                                  for name, model in base_learners.items()}
            self.train_base_learners(
                fold_base_learners, fold_xtrain, fold_ytrain, verbose=False)

            fold_P_base = self.predict_base_learners(
                fold_base_learners, fold_xtest, verbose=False)

            cv_preds.append(fold_P_base)
            cv_y.append(fold_ytest)
            print("Fold %i done" % (i + 1))

        print("CV-predictions done")

        # Be careful to get rows in the right order
        cv_preds = np.vstack(cv_preds)
        cv_y = np.hstack(cv_y)

        # Train meta learner
        print("Fitting meta learner...", end="")
        meta_learner.fit(cv_preds, cv_y)
        print("done")

        return base_learners, meta_learner

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
    # P = np.zeros((y_test.shape[0], 7))
    # P = pd.DataFrame(P)
    # print(P)
    # m = liu_utility.getDecisionTreeClassifier(X_train,y_train)
    # res = m.predict_proba(X_test)
    # print("roc_auc_score:%f" % roc_auc_score(y_test,res[:,1]))
    #
    # rm = liu_utility.getRandomForestClassifier(X_train,y_train,n_estimators=10,max_depth=3)
    # res1 = rm.predict_proba(X_test)

    # P = E.train_predict(models,X_train, X_test, y_train)
    # E.score_models(P,y_test)
    # E.plot_roc_curve(y_test, P.values, P.mean(axis=1), list(P.columns), "ensemble")

    meta_learner =  GradientBoostingClassifier(
    n_estimators=1000,
    loss="exponential",
    max_features=4,
    max_depth=3,
    subsample=0.5,
    learning_rate=0.005,
    random_state=SEED)
    xtrain_base, xpred_base, ytrain_base, ypred_base = train_test_split(
        X_train, y_train, test_size=0.5, random_state=SEED)
    models = E.get_models()
    # E.train_base_learners(models,xtrain_base,ytrain_base,True)
    # P_base = E.predict_base_learners(models, xpred_base)
    # meta_learner.fit(P_base, ypred_base)
    # P_pred, p = E.ensemble_predict(models,meta_learner,X_test)
    #
    # print("\nEnsemble ROC-AUC score: %.3f" % roc_auc_score(y_test, p))

    base_learners, meta_learner1 = E.stacking(models,clone(meta_learner),xtrain_base,ytrain_base,KFold(2))
    P_pred, p = E.ensemble_predict(base_learners, meta_learner1, X_test)
    print("\nEnsemble ROC-AUC score: %.3f" % roc_auc_score(y_test, p))

    sl = SuperLearner(
        folds=10,
        random_state=SEED,
        verbose=2,
        backend="multiprocessing"
    )

    # Add the base learners and the meta learner
    sl.add(list(models.values()), proba=True)
    sl.add_meta(meta_learner, proba=True)

    # Train the ensemble
    sl.fit(X_train, y_train)

    # Predict the test set
    p_sl = sl.predict_proba(X_test)

    print("\nSuper Learner ROC-AUC score: %.3f" % roc_auc_score(y_test, p_sl[:, 1]))


