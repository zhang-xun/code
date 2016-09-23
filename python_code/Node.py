#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_
"""
    class Node:
        value
        length= []
    (functions)
        addchild()
        depth_first()

"""
class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def __iter__(self):
        return iter(self._children)

    def addchild(self,child):
        self._children.append(child)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()



if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child3 = Node(3)
    child4 = Node(4)
    child5 = Node(5)
    root.addchild(child1)
    root.addchild(child2)
    child1.addchild(child3)
    child1.addchild(child4)
    child2.addchild(child5)

    for child in root.depth_first():
        print(child)

