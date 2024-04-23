#!/usr/bin/env python

class Factorial(object):
    def __init__(self, x):
        self.x = x
    def factorial(self):
        if self.x == 0:
            return 1
        else:
            n = self.x
            self.x -= 1
            return n * self.factorial()

input = int(input("Enter a number: "))
fact = Factorial(input)
print(f'{input} factorial = {fact.factorial()}')
