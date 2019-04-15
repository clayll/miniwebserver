from sklearn import neighbors
from sklearn import datasets

def irisShow():

    # 加载花的数据
    rs = datasets.load_iris()
    # 数据说明
    print(rs.DESCR)
    #特征值
    x = rs["data"]
    #目标值
    y = rs["target"]

    neighbors.KNeighborsClassifier(n_neighbors=5)

def neighbors_1():
    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]

    neigh = neighbors.KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X, y)
    print(neigh.predict([[1.1]]))  # 预测出所在类样本标签
    print(neigh.predict_proba([[0.9]]))  # 预测


if __name__ == '__main__':
    neighbors_1()
