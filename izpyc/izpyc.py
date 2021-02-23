from ctypes import *
from .prototypes import setup
from .space import Space

def space(izso):
    izlib = cdll.LoadLibrary(izso)
    setup(izlib)
    return Space(izlib)
