#!/usr/bin/env python

import pandas as pd

filename = 'memberinfo.csv'
df = pd.read_csv(filename, encoding='utf-8')
print(df)

newdf01 = df.set_index(keys=['id'])
print(newdf01)

newdf02 = df.set_index(keys=['id'], drop=False)
print(newdf02)

df02 = pd.read_csv(filename, index_col='id')
print(df02)