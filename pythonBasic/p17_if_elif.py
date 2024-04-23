#!/usr/bin/env python

# 양수 음수 제로

while True:
    i = input("Input the number(q : Quit) : ")
    if i == 'q':
        break
    elif i.isalpha():
        print("다시 입력해주세요.")
        continue
    else:
        if int(i) > 0:
            print("This is positive.")
        elif int(i) == 0 :
            print("This is zero.")
        else :
            print("This is negative.")
