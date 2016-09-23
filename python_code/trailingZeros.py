#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_

def divideZero(n):
    count  = 0
    index = 5
    while n / index >= 1:
        count += n // index
        index *= 5
    return count




if __name__=="__main__":
    print(divideZero(11))
    print(divideZero(111101010010100100))
    
