#!/usr/bin/env python

from pandas import Series

mylist = [10, 20, 30, 40]
myseries = Series(data=mylist, index=['김유신', '이순신', '강감찬', '광해군'])

print('\n Data Type')
print(type(myseries))

myseries.index.name = '점수'
print('\n Index name of Series')
print(myseries.name)

print('\n name of Index')
print(myseries.index)

print('\n value of Series')
print(myseries.values)

print('\n print information of Series')
print(myseries)

print('\n repeat print')
for idx in myseries.index:
    print('index : '+ idx + ', Values : ' + str(myseries[idx]))
