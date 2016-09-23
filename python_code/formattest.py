#! /usr/local/bin/python3
#_*_ coding:utf-8 _*_
"""
    format() has two useage:
        1.format( text, ">length")
            后一个参数接的是>（左对齐）^右对齐 <右对齐, 加上想要的宽度值length

        
        2."{:^s}   {:<s}".format("hello", "world")
"""
def main():
    print("useage1")
    print( format("hello world",'+^40'))
    print(format("hello world",'+>40'))
    print(format("hello world",'+<40'))

    print("useage2")

    
    print('{:^20} {:^20}'.format("hello","world"))
    print('{:<20} {:>20}'.format("hello","world"))
    print('{:>20} {:>20}'.format("hello","world"))



if __name__ == "__main__":
    main()
