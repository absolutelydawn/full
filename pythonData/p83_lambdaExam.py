#!/usr/bin/env python

def nolambda(x, y):
    return 3 * x + 2 * y

x, y = 3, 5

yeslambda = lambda x, y : 3 * x + 2 * y

result = yeslambda(x, y)
print("람다 방식 : %d" %(result))

