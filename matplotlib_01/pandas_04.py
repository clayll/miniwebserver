import pandas as pd
import numpy as np
import string

pd.set_option('display.max_columns', None)
df = pd.read_csv("starbucks_store_worldwide.csv")
# print(df.info())
# ca  cn

groupd = df.groupby(by=["Country","State/Province"])[["Country"]].count()
# print(groupd.loc[['CN'],"Country"])
# CNdf =
# print(CNdf)

df_index = pd.DataFrame(np.random.randint(1,20,(7,5)),index=list(string.ascii_letters[0:7]),columns=list(string.ascii_uppercase[-5:]))

print(df_index)
df1 = df_index.set_index(['X','Z'],drop = False)
print(df1.loc[["2","15"],"W"])