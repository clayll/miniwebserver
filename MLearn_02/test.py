import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import minmax_scale
import numpy as np
import jieba

# index = ['a','b']
# index2 = ["a","b"]
# pd1 = pd.Series(['hello',21],index=index)
# pd2 = pd.Series([3,9],index = index2)
# print(pd1*pd2)
#
# a = tf.constant(123,dtype=tf.int32)
# b = tf.constant(4,dtype=tf.int32)
# rst = tf.add(a,b)
# rst = tf.multiply(a,b)
# sess = tf.Session()
# print(sess.run(rst))
#
# a = tf.constant(123,dtype=tf.int32)
# b = tf.constant(4,dtype=tf.int32)
# rst = tf.add(a,b)
# rst = tf.multiply(a,b)
# sess = tf.Session()
# print(sess.run(rst))
#
#
# np.random.normal()
#
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# y= np.array([0,1,2])
# print(a[range(3),y])
#
# a = np.array([[1,3,1],[5,5,2],[15,8,9],[20,44,12]])
# # probs = a / np.sum(a, axis=1, keepdims=True)  # [N x K]
# # print(probs)
# y= np.array([0,1,0,1])
# # print(probs[range(4),y])
#
# probs = np.exp(a - np.max(a, axis=1, keepdims=True))
#
# probs /= np.sum(probs, axis=1, keepdims=True)
# loss = -np.sum(np.log(probs[np.arange(4), y])) / 4
# print(np.log(probs[np.arange(4), y]))
# print(loss)
# s = tf.truncated_normal((784,500),mean=0.1,stddev=0.1)
# sess = tf.Session()
# print(sess.run(s))

# 合并多个csv
def pd_tocsv():
    pdread1 = pd.read_csv(r"C:\Users\刘靓\Desktop\xa.txt",delimiter='\t',encoding='utf_8_sig')
    pdread1["city"] = '西安'
    pdread2 = pd.read_csv(r"C:\Users\刘靓\Desktop\wh.txt", delimiter='\t', encoding='utf_8_sig')
    pdread2["city"] = '武汉'
    pdread3 = pd.read_csv(r"C:\Users\刘靓\Desktop\bj.txt", delimiter='\t', encoding='utf_8_sig')
    pdread3["city"] = '北京'

    pdread4 = pd.read_csv(r"C:\Users\刘靓\Desktop\cd.txt", delimiter='\t', encoding='utf_8_sig')
    pdread4["city"] = '成都'

    pdread5 = pd.read_csv(r"C:\Users\刘靓\Desktop\gz.txt", delimiter='\t', encoding='utf_8_sig')
    pdread5["city"] = '广州'

    pdread6 = pd.read_csv(r"C:\Users\刘靓\Desktop\hz.txt", delimiter='\t', encoding='utf_8_sig')
    pdread6["city"] = '杭州'

    pdread7 = pd.read_csv(r"C:\Users\刘靓\Desktop\sh.txt", delimiter='\t', encoding='utf_8_sig')
    pdread7["city"] = '上海'

    pdread = pd.concat([pdread1,pdread2,pdread3,pdread4,pdread5,pdread6,pdread7],axis=0)

    pdread.to_csv(r'C:\Users\刘靓\Desktop\数据分析_词频.csv', header=True, index=False,encoding='utf_8_sig')

# 测试标准化
def testStander():
    np.random.seed(2)
    randrage =  np.random.randint(1,100,[10,1]).astype(dtype=np.float)
    print(randrage[:,0:1])
    randrage1 = StandardScaler().fit_transform(randrage)
    randrage2 = minmax_scale(randrage)
    print(randrage1)
    print(randrage2)

def KFlodTest():

    from sklearn.model_selection import KFold
    X = np.array([[1, 2], [3, 4], [1, 2], [3, 4],[4,5],[6,7]])
    y = np.array([1, 2, 3, 4,5,6])
    kf = KFold(n_splits=4)
    # kf.get_n_splits(X)

    for train_index, test_index in kf.split(X):

        print("TRAIN:", train_index, "TEST:", test_index)

        # print(X[train_index], X[test_index])
        # # ...
        # # y_train, y_test =
        # print(y[train_index], y[test_index])


def testTfidf():
    from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

    X_test = ['卡尔 敌法师 蓝胖子 小小', '卡尔 敌法师 蓝胖子 痛苦女王']

    tfidf = TfidfVectorizer()
    weight = tfidf.fit_transform(X_test).toarray()
    word = tfidf.get_feature_names()
    print(weight)
    for i in range(len(weight)):
        print(u"第", i, u"篇文章的tf-idf权重特征")
        for j in range(len(word)):
            print(word[j], weight[i][j])

def testCountVec():
    from sklearn.feature_extraction.text import CountVectorizer
    texts =["dog cat fish","dog cat cat","fish bird", 'bird']   # 为了简单期间，这里4句话我们就当做4篇文章了
    cv = CountVectorizer()  # 词频统计
    cv_fit = cv.fit_transform(texts)  # 转换数据
    # print(cv_fit.toarray())

    print(cv.fit_transform(texts))
    print("-------------------------")
    print(cv.transform(texts))
def testz_score():
    arr = np.array(np.random.randint(1,100,20))
    mean = arr.mean()
    std = arr.std()
    print(mean,std)
    arr1 =(arr-mean)/std
    print(arr)
    print(arr1)
    print(arr1.std())

def 清洗数据挖掘行业():
    f = pd.read_csv(r"C:\\myPython\\miniweb\\dataAnalysis\\dataAnalysis\\spss\\作业\\spss项目\\数据源\\清洗关键词v0.1\\数据挖掘清洗关键词1.csv")
    arr = "移动互联网,电商,教育,金融,服务,人工智能,社交,文娱,医疗,物流,工具,房产,消费生活,硬件,信息安全,汽车,其他,游戏,广告,旅游".split(",")
    for i in range(len(f.loc[:,["所属行业"]])):
        for content in arr:
            print(i)
            if str(f.loc[i,"所属行业"]).find(content) != -1:
                f.loc[i,"所属行业1"]=content
                break
    f.to_excel(r"C:\\myPython\\miniweb\\dataAnalysis\\dataAnalysis\\spss\\作业\\spss项目\\数据源\\清洗关键词v0.1\\数据挖掘清洗关键词2.xlsx")


def 清洗数据分析行业():
    f = pd.read_csv(r"C:\\myPython\\miniweb\\dataAnalysis\\dataAnalysis\\spss\\作业\\spss项目\\数据源\\清洗关键词v0.1\\数据分析清洗关键词1.csv")
    arr = "移动互联网,电商,教育,金融,服务,人工智能,社交,文娱,医疗,物流,工具,房产,消费生活,硬件,信息安全,汽车,其他,游戏,广告,旅游".split(",")

    for i in range(len(f.loc[:,["所属行业"]])):
        for content in arr:
            print(i)
            if str(f.loc[i,"所属行业"]).find(content) != -1:
                f.loc[i,"所属行业1"]=content
                break
    f.to_excel(r"C:\\myPython\\miniweb\\dataAnalysis\\dataAnalysis\\spss\\作业\\spss项目\\数据源\\清洗关键词v0.1\\数据分析清洗关键词2.xlsx")

def 处理数据分析():
    skilllist = "Sql,Python,R,Excel,Sas,Hive,Spss,Ppt,Bi,Hadoop,Tableau,Spark,Mysql,Java,Oracle,Linux,Office,Matlab,Svm,Erp,Scala,Pandas,Nlp,Tensorflow,Insights,Powerbi,Mongodb,Gekko,Hbase".upper().split(",")
    exl = pd.read_csv("E:\数据分析-ALL.csv")

    for i in skilllist:
        exl[i] = "F"

    for index,i in enumerate(exl["职位描述"]):
        i = jieba.lcut(str(i))
        s = [item.upper() for item in i if item.upper()  in skilllist]
        exl.loc[index, s ] = "T"

    exl.to_excel("e:\数据分析清洗关键词1.xlsx")

def 处理数据挖掘():
    skilllist = "Python,Spark,Hadoop,Java,C,Hive,Linux,Sql,R,Nlp,Scala,Hbase,Tensorflow,Svm,Shell,Sas,Storm,Caffe,Gbdt,Matlab,Mysql,Pandas,Xgboost,Numpy,Spss,Etl,Excel,Go,Learn,Scikit,Flink,Kaggle,Rnn,Theano,Pytorch,Sklearn,Java,python,Oracle,Bi,Keras,Mapreduce,Mllib".upper().split(",")
    exl = pd.read_csv("E:\数据挖掘-all输出.csv")

    for i in skilllist:
        exl[i] = "F"

    for index,i in enumerate(exl["职位描述"]):
        i = jieba.lcut(str(i))
        s = [item.upper() for item in i if item.upper()  in skilllist]
        exl.loc[index, s ] = "T"

    exl.to_excel("e:\数据挖掘   清洗关键词1.xlsx")

# testStander()

# KFlodTest()
# 定义不同力度的正则化惩罚力度
# c_param_range = [0.01, 0.1, 1, 10, 100]
# testz_score()
#
# results_table = pd.DataFrame({'c_param_range':c_param_range})
# # for i in range(5,2):
# #     print(i)
# # print(range(5,2))
#
# print(type(results_table.c_param_range.values))
# print(results_table['c_param_range'])
# testTfidf()
# testCountVec()

# 处理数据分析()
# 处理数据挖掘()

