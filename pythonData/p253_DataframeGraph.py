#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

plt.rcParams['font.family'] = ['NanumBarunGothic']

filename = 'dataframeGraph.csv'
myframe = pd.read_csv(filename, encoding='euc-kr')
myframe.set_index(keys='name')
print(myframe)


myframe.plot(title='someTitle', kind='line', figsize=(10, 6), legend=True)

filename = 'p253_dataframeGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved. . .')
plt.show()