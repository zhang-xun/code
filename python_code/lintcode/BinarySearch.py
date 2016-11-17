#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_

def binarySearch(nums, target):
    first,last = 0,len(nums)-1
    while first <= last:
        mid = (first + last ) // 2
        if target == nums[mid]:
            if nums[mid-1]!=target:
                return mid
            else:
                last=mid
                mid = mid-1
                
        if target > nums[mid]:
            first = mid + 1
        if target < nums[mid]:
            last = mid -1
            
    return -1



if __name__ == "__main__":
    print(binarySearch([4,5,9,9,12,13,14,15,15,18],10))
    print(binarySearch([1,4,4,5,7,7,8,9,9,10],1))
    print(binarySearch([3,4,5,8,8,8,8,10,13,14], 8))
