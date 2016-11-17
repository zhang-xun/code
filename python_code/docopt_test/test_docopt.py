#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_
"""Qingchat CLI

Usage:
      qingchat config ip <ip>
      qingchat config port <port>
      qingchat config login
      qingchat group list
      qingchat group choose <group_name>...
      qingchat group clean
      qingchat group send -t <content>
      qingchat group send -i <media>
      qingchat group send -f <file> [<delaytime>]
                      
      Options:
        -h --help     Show this screen.
        -v --version     Show version.
"""
from docopt import docopt

def try_docopt():
    args = docopt(__doc__,version = 'Qingchat 0.3.2')
    print(args)


if __name__ == "__main__":
    try_docopt()
