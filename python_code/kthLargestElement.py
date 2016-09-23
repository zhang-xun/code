#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_


def kthLargestElement(k,A):
    

    A1 = sorted(A)
    print(A1)
    while k > 1:
        k -= 1
        A1.pop()
    return A1.pop() 



if __name__ == "__main__":
    print(kthLargestElement(3,[9,3,2,4,8]))
