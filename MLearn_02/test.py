import pandas as pd


index = ['a','b']
index2 = ["a","b"]
pd1 = pd.Series(['hello',21],index=index)
pd2 = pd.Series([3,9],index = index2)
print(pd1*pd2)