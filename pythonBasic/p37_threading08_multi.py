#!/usr/bin/env python

import threading, time

data = 0

def generator(start, end):
    global data
    for _ in range(start, end+1):
        buf = data
        time.sleep(0.01)
        data = buf + 1

t1 = threading.Thread(target=generator, args=(1,10))
t2 = threading.Thread(target=generator, args=(1,10))

t1.start()
t2.start()

# join : 자식 thread가 증가되는 시점까지 기다려줌
t1.join()
t2.join()

print(data)