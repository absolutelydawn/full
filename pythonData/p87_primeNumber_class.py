#!/usr/bin/env python

import random

class Prime(object):
    def __init__(self, num):
        self.num = num

    def isprime(self):
        for k in range(2, self.num + 1):
            if self.num % k == 0:
                break
            if k == self.num:
                return True
            else:
                return False
prime = Prime(random.randint(2,10))
print(f'random number is {prime.num}')
print(f'{prime.num} is Prime number') if prime.isprime() else print(f'{prime.num} is not Prime number')

# class PrimeNumber(object):
#     def __init__(self, number):
#         self.number = number
#         self.primes = []
#
#     def isprime(self, number):
#         if number < 2:
#             return f'{number} is not a prime number'
#         else :
#             for i in range(2, number):
#                 if number % i == 0:
#                     return f'{number} is not a prime number'
#                 else:
#                     return f'{number} is a prime number'
#
# num = random.randrange(1, 10 + 1)
# prime = PrimeNumber(num)
#
# print(f'random number is {num}')
# print(prime.isprime(num))
