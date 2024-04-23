#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import re

plt.rcParams['font.family'] = 'NanumBarunGothic'

url = 'http://www.cgv.co.kr/movies'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

#info = soup.find_all('div', attrs={"class":"sect-movie-chart"})
t1 = soup.findAll('strong', attrs={'class': 'rank'})
t2 = soup.findAll('strong', attrs={'class': 'title'})
t3 = soup.findAll('span', attrs={'class': 'percent'})
t4 = soup.findAll('strong', attrs={'class': 'percent'})
t5 = soup.findAll('span', attrs={'class': 'txt-info'})
# print(t4)
# print(t5)

#pattern = re.compile('\d{4}.\d{2}.\d{2}')
pattern = re.compile('[^<strong>]\d{4}.\d{2}.\d{2}')
t11 = [i.text for i in t1]
t22 = [i.text for i in t2]
t33 = [i.text[:-1] for i in t3]
t44 = [i.text[3:6] for i in t4]
t55 = [pattern.findall(i.text)[0][1:] for i in t5]

# print(t11)
# print(t22)
print(t33)
#print(t44)
# print(t55)
#
# print(len(t11), len(t22), len(t33), len(t44), len(t55))

print('-' * 50)
#print(info)
print('-' * 50)
ttable = []

result = [[t11[i], t22[i], t33[i], t44[i], t55[i]] for i in range(len(t11))]

# print(result)

mycolumn = ['순위', '제목', '평점', '예매율', '개봉일']

myframe = DataFrame(result, columns=mycolumn)
newdf = myframe.set_index(keys=['순위'])
print(newdf)
print('-' * 40)

filename = 'cgvMovie.csv'
myframe.to_csv(filename, encoding='utf8', index=False)
print(filename, ' Saved...', sep='')
print('finisihed')

dfmovie = myframe.reindex(columns=['제목', '평점', '예매율'])
print(dfmovie)

mygroup0 = dfmovie['제목']
mygroup1 = dfmovie['평점']
mygroup2 = dfmovie['예매율']
mygroup2 = mygroup2.str.replace('%','')

df = pd.concat([mygroup1, mygroup2], axis=1)
df = df.set_index(mygroup0)
df.columns = ['평점', '예매율']
print(df)

df.astype(float).plot(kind='barh', title='영화별 평점과 예매율', rot=0)
filename = 'cgvMovieGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()