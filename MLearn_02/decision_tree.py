from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble.forest import RandomForestClassifier

def decision_frist():

    data = datasets.load_iris()
    x = data["data"]
    y = data["target"]

    X_train, X_test, y_train, y_test = train_test_split(x , y , test_size = 0.25)
    des = DecisionTreeClassifier(max_leaf_nodes=3)
    des.fit(X_train,y_train)
    print(des.predict(X_test))
    print(des.score(X_test,y_test))

    rom = RandomForestClassifier()
    rom.fit(X_train,y_train)
    print(rom.predict(X_test))
    print(rom.score(X_test, y_test))

if __name__ == '__main__':
    decision_frist()