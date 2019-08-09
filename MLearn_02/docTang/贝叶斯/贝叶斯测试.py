from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import jieba
import numpy as np

class Bayes_News():
    pass

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
                all_words.append(str(word))
            contents_clean.append(line_clean)
        return contents_clean, all_words


if __name__ == '__main__':
    # texts = ["dog cat fish", "dog cat cat", "fish bird", 'bird']
    # cv = CountVectorizer()
    # cv_fit = cv.fit_transform(texts)
    # print(cv_fit.toarray())
    bayesNews  = Bayes_News()
    data = bayesNews.get_Data()
    df_content = bayesNews.split_byJieba(data.content.values.tolist())
    df_stopwords = bayesNews.get_stopwords()
    contents_clean, all_words =bayesNews.drop_stopwords(df_content.values.tolist(),df_stopwords.values.tolist())
    df_content = pd.DataFrame({'contents_clean': contents_clean})
    print(all_words)
    df_all_words = pd.DataFrame({'all_words': all_words})

    #打印排行
    # print df.groupby(by='col1').agg({'col2':sum}).reset_index()
    # words_count = df_all_words.groupby(by=['all_words'])['all_words'].agg({"count": numpy.size})

    # words_count = df_all_words.groupby(by=['all_words'])['all_words'].agg({"count": np.size})
    # words_count = words_count.reset_index().sort_values(by=["count"], ascending=False)
    # print(words_count)

