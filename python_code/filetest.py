# coidng:utf-8

import os

files = open("tetris.py","r")

datas = [ file.strip() for file in files]

for data in datas:
    print(data)


print(1,os.linesep)
print(2,os.sep)
print(3,os.pathsep)
print(4,os.curdir)
print(5,os.pardir)
