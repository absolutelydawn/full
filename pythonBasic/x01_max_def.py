#!/usr/bin/env python

import random

def findMax(data):
    data = random.sample(range(1, 101), 10)
    max = 0
    for i in data:
        if i > max:
            max = i
    return data, max

print(findMax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


