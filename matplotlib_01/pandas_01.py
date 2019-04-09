import pandas as pd
import numpy as np
import string




x = pd.Series(np.random.randint(1,12,12),index=list(string.ascii_letters)[0:12])
# print(x[x>3])
# print(x)

x = pd.read_csv("dogNames2.csv")

s = np.arange(12).reshape(3,4)

f = pd.DataFrame(s,columns = ['a','b','c','d'],index=list(string.ascii_letters)[-3:])

# print(f.dtypes,f.info)
# print(f.sort_values(["a","d"], ascending=False))
# print(f)
# print(f.loc["Y":"Z",["b","d"]])

# print(f.iloc[0:2,1:3])




# print(x[x["Count_AnimalName"]>800])
#
# print(f[(f["d"]>5) | (f["a"]>5)])

f.iloc[0,1] = np.nan
f.iloc[1,2] = np.nan
f.iloc[2,3] =22
print(f.head(5))
# print(f.mean())
# print(f.fillna(f.median()))
# f.fillna
f[f==0]=np.nan

print(f[1:3]["d"])