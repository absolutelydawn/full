#!/usr/bin/env python
# 실행 순서를 보장하고 싶으면...

import threading, time

class sample(threading.Thread):
    def __init__(self, time):
        super(sample, self).__init__()
        self.time = time
        self.start()

    def run(self):
        print(self.time, "starts")
        for i in range(0, self.time):
            time.sleep(1)
        print(self.time, " has finished")

t3 = sample(3)
t2 = sample(2)
t1 = sample(1)
t3.join()
print("t3.join() has finished")
t2.join()
print("t2.join() has finished")
t1.join()
print("t1.join() has finished")
