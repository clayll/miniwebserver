from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier

from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.kernel_approximation import Nystroem
from sklearn.kernel_approximation import RBFSampler
from sklearn.pipeline import make_pipeline


def getDecisionTreeClassifier(X_train,y_train,
                              max_depth=3,max_leaf_nodes=5):
    m = DecisionTreeClassifier(max_depth=max_depth,max_leaf_nodes=max_leaf_nodes)
    m.fit(X_train,y_train)
    return m


def getDecisionTreeClassifier(X_train,y_train,
                              max_depth=3,max_leaf_nodes=5):
    m = DecisionTreeClassifier(max_depth=max_depth,max_leaf_nodes=max_leaf_nodes)
    m.fit(X_train,y_train)
    return m

def getRandomForestClassifier(X_train,y_train,n_estimators=100,max_depth=5,random_state=0):
    m = RandomForestClassifier(n_estimators=n_estimators,max_depth=5)
    m.fit(X_train,y_train)
    return m

def getGaussianNB(X_train,y_train):
    nb = GaussianNB()
    nb.fit(X_train,y_train)
    return nb

def getSVC(X_train,y_train,C=100, probability=True):
    svc = SVC(C=C, probability=probability)
    svc.fit(X_train, y_train)
    return svc

def getKNeighborsClassifier(X_train,y_train,n_neighbors=3):
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    return knn

def getLogisticRegression(X_train,y_train,random_state=0,C=100):
    lr = LogisticRegression(C=C, random_state=random_state)
    lr.fit(X_train, y_train)
    return lr

def getMLPClassifier(X_train,y_train,hidden_layer_sizes,early_stopping=False,random_state=0):
    nn = MLPClassifier(hidden_layer_sizes, early_stopping=early_stopping, random_state=random_state)
    nn.fit(X_train, y_train)
    return nn

def getGradientBoostingClassifier(X_train,y_train,random_state=0,n_estimators=100):
    gb = GradientBoostingClassifier(n_estimators=n_estimators, random_state=random_state)
    gb.fit(X_train, y_train)
    return gb

 # nb = GaussianNB()
 #    svc = SVC(C=100, probability=True)
 #    knn = KNeighborsClassifier(n_neighbors=3)
 #    lr = LogisticRegression(C=100, random_state=SEED)
 #    nn = MLPClassifier((80, 10), early_stopping=False, random_state=SEED)
 #    gb = GradientBoostingClassifier(n_estimators=100, random_state=SEED)
 #    rf = RandomForestClassifier(n_estimators=10, max_features=3, random_state=SEED)

