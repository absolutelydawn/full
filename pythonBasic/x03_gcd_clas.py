#!/usr/bin/env python

import random

def gcd(a, b):
    print("gcd", (a,b))
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f'gcd({a}, {b}) of {a}, {b} = {gcd(a, b)}')