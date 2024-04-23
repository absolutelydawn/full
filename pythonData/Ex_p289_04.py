#!/usr/bin/env python

from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['NanumBarunGothic']
# print([f.fname for f in matplotlib.font_manager.fontManager.ttflist])

mylist = [30, 20, 40, 60, 50]
myindex = ['이상화', '한용운', '노천명', '윤동주', '이육사']

print(myindex)
print(mylist)
print('-' * 50)

myseries = Series(mylist, index=myindex)
myylim = [0, myseries.max() + 10]
myseries.plot(title='금월 실적', kind='line', ylim=myylim, grid=False, rot=40, use_index=True, color=['b'])

filename = 'p289_seriesGraph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved . . .')
plt.show()