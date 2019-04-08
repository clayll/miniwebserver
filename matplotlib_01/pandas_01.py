import pandas as pd
import string

print()

x = pd.Series(range(10),index=list(string.ascii_letters)[0:10])
print(x[x>3])