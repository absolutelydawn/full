#!/usr/bin/env python

import random

class Calculate(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

a = random.randrange(1, 20 + 1)
b = random.randrange(1, 10 + 1)

calc = Calculate(a, b)

print (f'first : {a}, second : {b}')

print(f'{a} + {b} = {calc.add()}')
print(f'{a} - {b} = {calc.sub()}')
print(f'{a} * {b} = {calc.mul()}')
print(f'{a} / {b} = {round(calc.div(), 4)}')