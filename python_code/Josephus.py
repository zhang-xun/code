#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_


class LinkNode:
    def __init__(self,value):
        self.value=value
        self.next=None

def printcycle(head):
    while head.next.value != 1:
        print(head.next.value)
        head = head.next

def creatcyle(total):
    head = LinkNode(1)
    prev =head 
    index = 2
    while total - 1 > 0:
        node = LinkNode(index)
        prev.next = node
        prev = node
        total -= 1
        index += 1
    prev.next = head
    #printcycle(head)
    return head



def josephus(total,offset):
    index = 1
    start = 1
    prev = None
    head = creatcyle(total)

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
                head = prev
            index = 0
        else:
            prev = head
            head = head.next        
            index += 1



if __name__ == "__main__":
    josephus(41,3)
    #creatcyle(10)
