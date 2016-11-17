#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_

class LinkNode:
    def __init__(self,value):
        self.value = value
        self.next = None


def createcycle(total):
    head = LinkNode(1)
    prev = head
    index = 2
    while total - 1 > 0:
        curr = LinkNode(index)
        prev.next = curr
        prev = curr
        index += 1
        total -= 1
    prev.next = head
    return head


def josephus(total, offset):
    head = createcycle(total)
    index = 1
    start = 1
    prev = None

    while head and head.next:
        if index == offset:
            print(head.value)
            if start == offset:
                prev = head.next
                head.next = None
                head = prev

            else:
                prev.next = head.next
                head.next = None
                head = prev.next

            index = 1 
        else:
            prev = head
            head = head.next
            index += 1
        

if __name__ == "__main__":
    josephus(41,3)
