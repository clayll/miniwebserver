import snownlp
import matplotlib.pyplot as plt
import pandas as pd
import re



class SentimentAnalysis():
    def __init__(self):
        self.data = []
        self.result = []

    def dataClean(self):
        data = pd.read_csv(u"./datas/中国好声音.txt", delimiter="/n", encoding="utf-8")
        # cleanData = []
        # print(type(self.data))
        patten = re.compile("\d+\.\xa0|！+|？+")
        for i in range(len(data)):
            self.data.append(patten.sub("",data.iloc[i,0]))

    def sentimentDeal(self):
        self.result = [0, 0,  0]
        for i in range(len(self.data)):
            v = snownlp.SnowNLP(self.data[i]).sentiments

            if v <=0.33:
                self.result[0] += 1
            elif v > 0.33 and v <=0.66:
                self.result[1]  += 1
            else:
                self.result[2]  += 1


    def plt(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.xticks([0,0.5,1],["消极","中立","积极"])
        plt.bar([0,0.5,1],self.result,width=0.3,color="rcy")
        plt.title(u"中国好声音百度贴吧分析")
        plt.show()

if __name__ == '__main__':
    sentimentAna = SentimentAnalysis()
    sentimentAna.dataClean()
    sentimentAna.sentimentDeal()
    sentimentAna.plt()