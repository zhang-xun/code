#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_


from itertools import chain
def mergeSortedArray(A,B):
    result = []
    for i in chain(A,B):
        result.append(i)

    print(sorted(result))
    return sorted(result)


    




if __name__ == "__main__":
    mergeSortedArray([1,2,3,4],[2,4,5,6])
