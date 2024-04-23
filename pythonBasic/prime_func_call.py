#!/usr/bin/env python

import prime_func

# a = int(input("Enter a number (0 : Quit): "))

# if int(a) == 0 | int(a) == 1 :
#     print("re-enter number~!!")
#     quit()
# else :
#     prime_func.prime(a)

while True:
    n = int(input("Input number (0 : Quit) :  " ))

    if n == 0 :
        break
    if (n < 2):
        print("re-enter number~!!")
        continue
    print(f'{n} is prime number') if prime_func.prime(n) == 1 else print(f'{n} is NOT prime number')