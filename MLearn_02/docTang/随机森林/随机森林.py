from   docTang.线性回归.信用卡欺诈 import *
from sklearn.datasets import california_housing
from sklearn.model_selection import  train_test_split
from sklearn.tree import  DecisionTreeRegressor
import pydotplus
from sklearn import tree
from IPython.display import Image
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import os


class DecisionTreeDemo:
    def __init__(self):
        self.data = california_housing.fetch_california_housing()


        self.X_train, self.X_test, self.y_train, self.y_test =\
            train_test_split(self.data.data,self.data.target,random_state=42,test_size=0.2)


    def getTreeModel(self):
        d = DecisionTreeRegressor(max_depth=5)
        d.fit(self.X_train,self.y_train)
        return d

    def showGraph(self,model):
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
        graph.write_png("dtr_white_background.png")

    def getForestModel(self):
        model = RandomForestRegressor(random_state=42,n_estimators=20)
        model.fit(self.X_train, self.y_train)
        return model
    def gridValidate(self):
        tree_param_grid = {'min_samples_split': list((3, 6, 9)), 'n_estimators': list((10, 50, 100))}
        grid = GridSearchCV(self.getForestModel(),tree_param_grid,cv = 5)


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


if __name__ == '__main__':
    d = DecisionTreeDemo()
    # model  =  d.getTreeModel()
    # # d.showGraph(model)
    # print(model.score(d.X_test, d.y_test))
    #
    # model1 = d.getForestModel()
    # print(model1.score(d.X_test, d.y_test))

    d.gridValidate()


