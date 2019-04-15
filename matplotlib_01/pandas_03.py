import pandas as pd
import numpy as np


df = pd.read_csv("IMDB-Movie-Data.csv")
# print(df.info())


ge1 = df["Genre"]

gen = [m for i in ge1.str.split(',').tolist() for m in i]

set1 = list(set(gen))

x =  pd.Series(np.array(gen))

y = np.zeros((len(gen),2))


# gen1 = np.array(gen1)
# gen1 = pd.Series(gen1).groupby()
# print(gen1)
gen1 = pd.DataFrame(y,index=[i for i in range(len(x))],columns=["Genre","count"])
gen1["Genre"] = x
grouped = gen1.groupby("Genre").count()
print(grouped)
for i in grouped:
    print(i)


# gen2 = set()
# print(gen2)
#
# gen3 = pd.DataFrame(np.array(gen2).reshape(ge1.shape[0],len(gen2)))


gen2 = pd.DataFrame(np.array(np.zeros((gen1.shape[0],len(set1) ))),columns=set1)

for i in range(len(gen)):
    gen2.loc[i,gen[i]] = 1


print(gen2)
print(df.join(gen2))



