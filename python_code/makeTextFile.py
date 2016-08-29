#! /usr/bin/env python3
"""
    input a filename 
    write content
    write content to file( name after our filename) 
"""

import os
import math
ls = os.linesep

#input the filename

while True:
    filename = input("input  the filename:")
    if(os.path.exists(filename)):
        print("%s is exist,please try again!" %filename)
    else:
        break


lines = []
#get the content
while True:
    line = input("write your line content(. to exit)")
    if(line == "."):
        break
    else:
        lines.append(line)


file = open(filename,"w")
file.writelines(["%s%s" %(li,ls)  for li in lines])
file.close()
print("done")
