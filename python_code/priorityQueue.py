#! /usr/local/bin/python3
"""
    create class priorityqueue 
    create class Item

    __main__ test
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "Item(%s)" %self.name



if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item("foo"),1)
    q.push(Item("bar"),2)
    q.push(Item("zyn"),3)
    q.push(Item("zx"),4)

    print(q.pop())
    print(q.pop())
