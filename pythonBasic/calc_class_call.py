#!/usr/bin/env python

import calc_class

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

my = calc_class.Calc(a,b)

print(f'{a} + {b} = {my.add()}')
print(f'{a} - {b} = {my.sub()}')