#! /usr/local/bin/python3
"""
    let user choose :
        1.write new file 
        2.read exits file

    write new file:
        1).input the name you want to create
        2).memory the content
        3).write the content to the file

    read exits file:
        1).input the file alread exits
        2).read the content from the file(try except else )

"""
import os
ls = os.linesep

def writeNewFile():
    while True:
        filename = input("please input your wanted filename:")
        if os.path.exists(filename):
            print("%s is already exist, please try again!"%filename)
        else:
            break
    lines=[]
    while True:
        content = input("input your content(. to exit):")
        if content==".":
            break
        lines.append(content)
    
    fileobj = open(filename,"w")
    fileobj.writelines(["%s%s"%(line,ls) for line in lines])
    fileobj.close()
    print("write done")


def readOldFile():
    filename = input("input the file you want to read:")
    try:
        fileobj = open(filename,"r")
    except IOError as e:
        print("*** can not open ",e)
    else:
        lines=[line.strip() for line in fileobj ]
        for line in lines:
            print(line)
        fileobj.close()


def main():
    while True:
        choose=input("""
        1. write new file
        2. read old file
        e. exits\n
        """)
        if choose=="1":
            writeNewFile()
        elif choose=="e":
            break
        elif choose=='2':
            readOldFile()
        else:
            print("wrong paragram,try again!")
            continue


if __name__ == "__main__":
    main()
