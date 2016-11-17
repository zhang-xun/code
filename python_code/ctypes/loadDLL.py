#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_

import ctypes
from ctypes import *
import os

_file = "libsample.so"
_path = os.path.join(*(os.path.split(__file__)[:-1]+(_file,)))
_mod  = ctypes.cdll.LoadLibrary(_path)

gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype  = ctypes.c_int



if __name__ == "__main__":
   pass 
