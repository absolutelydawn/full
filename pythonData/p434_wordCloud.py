#!/usr/bin/env python

import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'steve.txt'
myfile = open(filename, 'rt', encoding='utf-8')

text = myfile.read()

wordcloud = WordCloud()
wordcloud = wordcloud.generate(text)
print(type(wordcloud))
print('-' * 50)

bindo = wordcloud.words_
print(type(bindo))
print('-' * 50)

sortedData = sorted(bindo.items(), key=lambda x: x[1], reverse=True)
print(sortedData)
print('-' * 50)

chartData = sortedData[0:10]
print(chartData)
print('-' * 50)

xtick = []
chart = []
for item in chartData:
    xtick.append(item[0])
    chart.append(item[1])

mycolor = ['r', 'g', 'b', 'm', 'c', '#FFF0F0', '#CCFFBB', '#05CCFF', '#11CCFF']
plt.bar(xtick, chart, color=mycolor)
plt.title('상위 빈도 Top 10')
filename = 'wordcloud01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file Saved . . .')

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud)
plt.axis('off')

filename = 'wordcloud02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file Saved . . .')