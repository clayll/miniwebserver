
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import naive_bayes

def news_bayes():
    # 获取数据
    news = datasets.fetch_20newsgroups(subset="all")
    # print(news.DESCR)
    newsData = news["data"]
    newsTarget = news["target"]
    # print(newsData[0:1])
    # print(newsTarget[0:1])
    # 把数据分为测试集合训练集
    x_train, x_test, y_train, y_test = train_test_split(newsData,newsTarget,test_size=0.25)


    # 文本特征转换
    count_vec = CountVectorizer()
    x_train = count_vec.fit_transform(x_train)
    x_test = count_vec.transform(x_test)

    nb = naive_bayes.MultinomialNB(alpha=1.0)
    nb.fit(x_train,y_train)
    prodict = nb.predict(x_test)

    print(prodict)
    print(nb.predict_proba(x_test))



if __name__ == '__main__':
    news_bayes()