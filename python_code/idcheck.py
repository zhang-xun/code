#! _*_coding_*_:utf-8
#! /usr/local/bin/python3

"""
    check the  identifier 
        must be start with alpha + _
        other char must be alpha + number + _

"""

import string

alpha=string.ascii_letters+"_"
number=string.digits

def idcheck():
    print("welcome to the identifier check version 1")
    print("string length more than 2")

    
    identifier=input("input the indentifier to be checked:")
    if(len(identifier)> 1):
        if identifier[0] not in alpha:
            print("不能以除了字母和下划线的字符开头:")
        else:
            for otherchar in identifier[1:]:
                if otherchar not in alpha+number:
                    print("标识符中含有非法字符")

            else:
                print("正确的标识符")



if __name__ == "__main__":
    print(alpha)
    print(number)
    idcheck()


