#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['NanumBarunGothic']

filename = 'mygraph.csv'

myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')

# print(myframe.head())
myframe.index.name = '이름'
myframe.columns.name = '시험 과목'


ymax = myframe.sum(axis=1)
ymaxlimit = ymax.max() + 10

myframe.plot(kind='bar', ylim=[0, ymaxlimit], rot=0, stacked=True, title='학생별 누적 시험 점수', legend=True)
filename = 'Ex_p239_Graph02_04.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print('-' * 50)
print(filename + ' Saved. . .')
print('-' * 50)

plt.show()


