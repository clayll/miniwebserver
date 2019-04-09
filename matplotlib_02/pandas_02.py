import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("IMDB-Movie-Data.csv")
print(df.info())

# x = df["Actors"].str.split(',').tolist()
# print(df["Rating"].mean())
# print(len([m for i in x for m in i]))


"""01 直方图
rdf = df.loc[:,["Title","Rating"]]
re = df.loc[:,["Rating","Runtime (Minutes)"]]
g_num = (re["Rating"].max() - re["Rating"].min())
print(re["Rating"].max())
y = re["Runtime (Minutes)"].tolist()
x = re["Rating"].tolist()
x_ticks = [round(i*0.7+1.9,1) for i in range(10)]
x_ticks.append(9.1)
print(x_ticks)
plt.figure(figsize=(20,10),dpi=80)
plt.xticks(x_ticks)
plt.hist(x,x_ticks,label="直方图",color='c')
plt.show()
"""

"""
统计电影分类(genre)的情况
genreO = list(df["Genre"].str.split(','))
genre1 = [m for i in genreO for m in i]
genre = set(genre1)
genre_data = pd.DataFrame(np.zeros((df.shape[0],len(genre)),dtype=np.int),columns=genre)
for i in range(df.shape[0]):
    row = df.loc[i,"Genre"]

    genre_data.loc[i,row.split(",")]=1

print(genre_data.sum())
# pd.set_option('display.max_columns', None)
print(df.join(genre_data))
"""
