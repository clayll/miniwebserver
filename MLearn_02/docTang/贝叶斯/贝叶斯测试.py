from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import jieba
import numpy as np
from jieba.analyse import extract_tags

class Bayes_News():
    def get_Data(self):
        data =  pd.read_table("data/data.txt",names=['category','theme','URL','content'],encoding='utf-8')
        data.dropna()
        return data

    def split_byJieba(self,data):
        rs = []

        for i in data:
            rs.append(jieba.lcut(i))

        return pd.DataFrame({'content_S':rs})

    def get_stopwords(self):
        stopwords=pd.read_csv("stopwords.txt",index_col=False,sep="\t",quoting=3,names=['stopword'], encoding='utf-8')
        return stopwords

    def drop_stopwords(self,contents,stopwords):
        contents_clean = []
        all_words = []
        for line in contents:
            line_clean = []
            for word in line:
                if word in stopwords:
                    continue
                line_clean.append(word)
                all_words.append(word)
            contents_clean.append(line_clean)
        return contents_clean, all_words

    def wordcloud(self,all_words):
        df_all_words = pd.DataFrame({'all_words': all_words})
        words_count = df_all_words.groupby(by=['all_words'])['all_words'].agg({"count": np.size})
        words_count = words_count.reset_index().sort_values(by=["count"], ascending=False)
        return words_count,df_all_words

    def jiebaAnalysisContent(self,df_content):

        for i in range(len(df_content.contents_clean)):
            content = "".join(df_content.contents_clean[i])
            df_content.contents_clean[i] =  extract_tags(content, topK=10, withWeight=True)

        return df_content

    def getlistToStr(self,x_train):
        words = []
        for line_index in range(len(x_train)):
            try:
                # x_train[line_index][word_index] = str(x_train[line_index][word_index])
                word = []
                for i in range(len(x_train[line_index])):
                    word.append(x_train[line_index][i][0])

                words.append(' '.join(word))
            except Exception as e:
                print(e,line_index)
        return words

    def getlistToStr2(self,x_train):
        words = []
        for line_index in range(len(x_train)):
            try:
                # x_train[line_index][word_index] = str(x_train[line_index][word_index])
                word = []
                for i in range(len(x_train[line_index])):
                    word.append(x_train[line_index][i])

                words.append(' '.join(word))
            except Exception as e:
                print(e,line_index)
        return words

    def getlistToStr3(self,x_train):
        words = []
        for line_index in range(len(x_train)):
            try:
                # x_train[line_index][word_index] = str(x_train[line_index][word_index])
                words.append(' '.join(X_train[line_index]))


            except Exception as e:
                print(e,line_index)
        return words

if __name__ == '__main__':
    # texts = ["dog cat fish", "dog cat cat", "fish bird", 'bird']
    # cv = CountVectorizer()
    # cv_fit = cv.fit_transform(texts)
    # print(cv_fit.toarray())
    bayesNews  = Bayes_News()
    data = bayesNews.get_Data()
    df_content = bayesNews.split_byJieba(data.content.values.tolist())
    df_stopwords = bayesNews.get_stopwords()
    contents_clean, all_words =bayesNews.drop_stopwords(df_content.content_S.values.tolist(),df_stopwords.stopword.values.tolist())
    df_contents = pd.DataFrame({'contents_clean': contents_clean})

    # content = "".join(df_content.contents_clean[2000])
    # content = extract_tags(content, topK=10, withWeight=True)
    # bayesNews.jiebaAnalysisContent(df_contents)

    df_train = pd.DataFrame({'contents_clean':df_contents.contents_clean,'label':data.category})
    label_mapping = {"汽车": 1, "财经": 2, "科技": 3, "健康": 4, "体育": 5, "教育": 6, "文化": 7, "军事": 8, "娱乐": 9, "时尚": 0}
    df_train['label'] = df_train['label'].map(label_mapping)  # 构建一个映射方法

    print(df_train.head())


    X_train, X_test, y_train, y_test = train_test_split( df_train['contents_clean'].values, df_train['label'].values,  random_state=1)


    vec = CountVectorizer(analyzer='word', max_features=4000,  lowercase = False)
    feature = vec.fit_transform(bayesNews.getlistToStr3(X_train))
    print(feature.shape)

    nb = MultinomialNB(class_prior=None, fit_prior=True)
    nb.fit(feature,y_train)
    testWords = bayesNews.getlistToStr3(X_test)

    print(nb.score(feature,y_train))

