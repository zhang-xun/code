#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_


def digitCounts(k,n):
    count = 0
    for i in range(n):
        if str(k) in list(str(i)):
            print(list(str(i))) 
            count += 1
    
    return count





if __name__ =="__main__":
    print(digitCounts(1,12))
