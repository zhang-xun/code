#! /usr/local/bin/python3
# _*_ coding:utf-8  _*_


class LinkNode:
    def __init__(self,item):
        self.item=item
        self.next=None

    def __repr__(self):
        return "Node{" + str(self.item) + "}"

if __name__ == "__main__":
    a = LinkNode(121)

    print(a.item)
    print(a)
