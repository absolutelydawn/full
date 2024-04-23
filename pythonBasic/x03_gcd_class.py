#!/usr/bin/env python

import random

class GCD(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gcd(self):
        print("gcd", (self.a, self.b))
        while self.b != 0:
            r = self.a % self.b
            self.a = self.b
            self.b = r
            print("gcd", (self.a, self.b))
        return self.a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd1 = GCD(a,b)
print(f'gcd({a}, {b}) of {a}, {b} : {gcd1.gcd()}')


# class GCD(object):
#     def gcd(a, b):
#         print(f'({a},{b})')
#         while b != 0:
#             a, b = b, a%b
#             print(f'({a},{b})')
#             if b == 0:
#                 return a
#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
#
# print(f'gcd({a}, {b}) of {a}, {b} : {GCD.gcd(a, b)}')