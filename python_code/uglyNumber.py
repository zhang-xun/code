#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_

def uglyNumber(n):
    while n % 2 == 0:
        n /= 2
    while n % 3 ==0:
        n /=3
    while n % 5 ==0:
        n/=5
    if n==1:
        return True
    else:
        return False

def nthUglyNumber(m):
    if m <= 0:
        return 0
    index = 0
    count = 0 
    while index <  m:
        count += 1
        if uglyNumber(count):
            index += 1
    return count



if __name__ == "__main__":
     print(nthUglyNumber(599))
     print(nthUglyNumber(2))
     print(nthUglyNumber(3))
     print(nthUglyNumber(4))
     print(nthUglyNumber(5))
     print(nthUglyNumber(6))
     print(nthUglyNumber(7))
     print(nthUglyNumber(8))
     print(nthUglyNumber(9))
