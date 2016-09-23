#! /usr/local/bin/python3
# _*_  coding:utf-8 _*_
"""
    如果我们在类中实现了__reversed__() 方法，就可以在自定义的类上实现反向迭代
"""

class CountDown:
    def __init__(self,start):
        self._start = start


    def __iter__(self):
        n = self._start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self._start:
            yield n
            n += 1


if __name__ == '__main__':
    c = CountDown(10)

    print("iter test")
    for i in c:
        print(i)

    print("reversed test")
    for i in reversed(c):
        print(i) 

