import pandas as pd
import numpy as np

ds1 = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
print(ds1)
ls1 = []

for i in ds1.index:
    for j in ds1.loc[i]:
        ls1.append(j)

ds2 = pd.Series(ls1)
print(ds2)
