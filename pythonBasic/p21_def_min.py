#!/usr/bin/env python

def min(a, b):
    if a > b :
        return b
    else:
        return a

a = int(input("Input the first number : "))
b = int(input("Input the second number : "))

print("{} vs {} : Min number = {}".format(a, b, min(a, b)))