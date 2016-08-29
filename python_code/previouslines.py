#! /usr/local/bin/python3
"""
    open a file 
        find a pattern, and then print the previous lines.
"""

from collections import deque

def search(lines,pattern,history=5):
    previous_lines=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open("previous.txt") as f:
        for line,previous_lines in search(f,"python",5):
            print("previous_lines")
            for previous_line in previous_lines:
                print("\t",previous_line,end="")
            print("currentline")
            print("\t",line)
            print("--"*20)
