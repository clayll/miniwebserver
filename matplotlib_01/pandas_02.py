import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np

df = pd.read_csv("IMDB-Movie-Data.csv")
print(df.info())
rdf = df.loc[:,["Title","Rating"]]
# x = df["Actors"].str.split(',').tolist()
# print(df["Rating"].mean())
# print(len([m for i in x for m in i]))

re = df.loc[:,["Rating","Runtime (Minutes)"]]
print(re.info())
print(re["Rating"].max(),re["Rating"].min())

g_num = 50
x = re["Rating"].tolist()
y = re["Runtime (Minutes)"].tolist()
x_ticks = [i*g_num for i in range(21)]
plt.figure(figsize=(20,8),dpi=8)
plt.xticks(x,x_ticks)
plt.scatter(x,y)
plt.show()
