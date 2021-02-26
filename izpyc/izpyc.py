from ctypes import *
from ctypes.util import find_library
from .prototypes import setup
from .space import Space

def space(izso=None):
    if izso is None:
        izso = find_library("iz")

    izlib = cdll.LoadLibrary(izso)
    setup(izlib)
    return Space(izlib)
