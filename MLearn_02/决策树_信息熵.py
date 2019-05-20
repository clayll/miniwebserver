import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn import preprocessing

class  Entropy():
    def __init__(self):
        pd.set_option('display.max_columns', None)
        self.data = pd.read_csv("./datas/AllElectronics.csv")
        # 定义两个列表
        self.featureList = []
        self.labelList = []
    def preData(self):
        data = self.data.iloc[:,1:]

        for i in range(len(data)):

            item = {"age" : data.iloc[i,0],
                    "income" : data.iloc[i,1],
                    "student": data.iloc[i,2],
                    "credit_rating" : data.iloc[i,3]}
            item_y = {"class_buys_computer" :  data.iloc[i,4]}
            self.featureList.append(item)
            self.labelList.append(item_y)

        dictVector = DictVectorizer()
        x_data = dictVector.fit_transform(self.featureList).toarray()
        print(x_data)
        print(dictVector.get_feature_names())

        dictVector2 = DictVectorizer()
        y_data = dictVector2.fit_transform(self.labelList).toarray()

        print(dictVector2.get_feature_names())
        treeClassifier = tree.DecisionTreeClassifier(criterion="entropy")
        treeClassifier.fit(x_data,y_data)

        x_test = x_data[0].reshape(1,-1)
        print(x_test)
        print(treeClassifier.predict(x_test))
        print(y_data[0])
        import graphviz

        dot_data = tree.export_graphviz(treeClassifier,
                                        out_file=None,
                                        feature_names=dictVector.get_feature_names(),
                                        class_names=dictVector2.get_feature_names(),
                                        filled=True,
                                        rounded=True,
                                        special_characters=True)
        graph = graphviz.Source(dot_data)
        # graph.render('./datas/pdffiles/computer')

    def preFeature(self):
        hot = preprocessing.OneHotEncoder()
        print(self.data)
        data = pd.get_dummies(self.data[["age","income","student","credit_rating"]])
        data1 = data.to_dict(orient="list")
        featureList=[]
        labels=[]


        for k,v in data1.items():
            labels.append(k)
            featureList.append(v)





class CartTree():
    def __init__(self):
        self.data = pd.read_csv("./datas/cart.csv")
        self.labels=[]
        self.x_data=[]
        self.y_data=[]

    def prepareData(self):

        datas = self.data.to_dict(orient="list")
        datas.pop('RID')
        for k,v in datas.items():
            self.labels.append(k)
            self.x_data.append(v[0:-1])
            self.y_data.append(v[-1:])

    def treeModel(self):
        treeClassifier = tree.DecisionTreeClassifier()
        treeClassifier.fit(self.x_data, self.y_data)
        print(treeClassifier.score(self.x_data,self.y_data))

if __name__ == '__main__':
     entropy = Entropy()
     entropy.preData()

     entropy.preFeature()
     # featureList = entropy.data.iloc[:,1:-1].to_dict()

     # featureList = entropy.data.iloc[:,1:-1]
     # print(featureList)

     # vec = DictVectorizer()
     # x_data = vec.fit_transform(featureList).toarray()
     # print(x_data)
     # ['age=middle_aged', 'age=senior', 'age=youth', 'credit_rating=excellent', 'credit_rating=fair', 'income=high', 'income=low', 'income=medium', 'student=no', 'student=yes']