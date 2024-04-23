#!/usr/bin/env python

## def prime(i):
##    if i%2 == 0:
##        print (f'{i} is not prime number')
##    else :
##        print(f'{i} is prime number')

def prime(n):
    for k in range (2, n+1):
        if n % k == 0:
            break
    if k == n :
        return 1
    else:
        return 0