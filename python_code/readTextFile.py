#! /usr/local/bin/python3
"""
    input the filename you want to read
    
    try catch else the open() function

"""


filename = input("input the filename you want to read:")
print("\n")

try:

    fileobj = open(filename,"r")
except IOError as  e:
    print("*** can not open ", e)
else:
    lines = [line.strip() for line in fileobj]
    for line in lines:
        print(line,)
    fileobj.close()

