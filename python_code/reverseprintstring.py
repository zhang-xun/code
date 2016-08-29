#! /usr/local/bin/python3
"""
    before:"abcdef"
    after:
        abcdef
        abcde
        abcd
        abc
        ab
        a

"""


def reversePrint(s):
    for i in range(-1,-len(s),-1):
        print(s[:i])



if __name__ == "__main__":
    reversePrint("abcdefg")

