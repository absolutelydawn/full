#!/usr/bin/env python
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame as df
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['NanumBarunGothic']

html = open('ex5-10.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one('body')
table = soup.find('tbody')
# print(table)

list = []
for row in table.find_all('td'):
    list.append(row.text)

print(list)
print('-' * 50)

list = np.reshape(np.array(list), (4, 3))
# print(list)

mycolumns = ['이름', '국어', '영어']
myframe = pd.DataFrame(list, columns=mycolumns)
myframe.set_index('이름', inplace=True)
print(myframe)
print('-' * 50)

myframe.astype(float).plot(kind='line', title='Score', legend=True)

filename = 'scoreGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved. . . .')
plt.show()
