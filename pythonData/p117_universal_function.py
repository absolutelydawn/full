#!/usr/bin/env python

import numpy as np

array = np.array([1.57, 2.48, 3.93, 4.33])
print('\n array print')
print(array)

print('\n np.ceil() function')
result = np.ceil(array)
print(result)

print('\n np.floor() function')
result = np.floor(array)
print(result)

print('\n np.round() function')
result = np.round(array)
print(result)

print('\n decimal place function')
result = np.round(array, 1)
print(result)

print('\n np.sqrt() function')
result = np.sqrt(array)
print(result)

arr = np.arange(10)
print(arr)
print(result)

print('\n exp() function')
result = np.exp(array)
print(result)

x = [5, 4]
y = [6, 3]

print('\n np.maximum() funciton')
result = np.maximum(x, y)
print(result)

print('-'*30)

array1 = np.array([-1.1, 2.2, 3.3, 4.4])
print('\n array1 print')
print(array1)

array2 = np.array([1.1, 2.2, 3.3, 4.4])
print('\n array2 print')
print(array2)

print('\n abs() function')
result = np.abs(array1)
print(result)

print('\n sum() function')
result = np.sum(array1)
print(result)

print('\n compare() funciton')
result = np.equal(array1, array2)
print(result)
