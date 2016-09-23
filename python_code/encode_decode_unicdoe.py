#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_
"""
    test for : str.encode()
             bytes.decode()
"""


import os

CODEC = 'utf-8'

def main():
    with open("text1","w") as f:
        string_out = u"hello world"
        print("string_type:",type(string_out))
        bytes_out  = string_out.encode(CODEC)
        print(type("bytes_type"),bytes_out)
        f.write(string_out)


    with open('text1','r') as fin:
        bytes_in = fin.read()
        print(type(bytes_in))
        print(bytes_in)



if __name__ == "__main__":
    main()



