#!/usr/bin/env python

def min(a, b):
    return b if a > b else a

a = int(input("Input the first number : "))
b = int(input("Input the second number : "))

print("{} vs {} : Min number = {}".format(a, b, min(a, b)))