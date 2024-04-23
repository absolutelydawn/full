#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

chickenfile = 'chicken.csv'
columns = ['지역', '브랜드', '매장수']
myframe = pd.read_csv(chickenfile, names=columns, header=None)
print(myframe)
print('-' * 50)

mygrouping = myframe.groupby('브랜드')['매장수']
sumSeries = mygrouping.sum()
sumSeries.index.name = '브랜드'
print(sumSeries)
print('-' * 50)

mycolor = ['red', 'green', 'blue']
mytitle = '브랜드 별 매장 개수'
myylim = [0, sumSeries.max() + 5]
myalpha = 0.7

sumSeries.plot(kind='bar', color=mycolor, title=mytitle, alpha=myalpha, legend=False, rot=15, ylim=myylim, grid=False)

filename = 'xx_chicken.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()

print('finished...')