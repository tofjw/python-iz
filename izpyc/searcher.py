from ctypes import *
from .util import iz_bool
from .space import Space

class SimpleSearcher:
    def __init__(self, x):
        self.variables = x
        self.size = len(x)

        VARSTYPE = c_void_p * self.size
        self.array = VARSTYPE()

        for i, v in enumerate(self.variables):
            self.array[i] = v.p

        FFVTYPE = CFUNCTYPE(c_void_p, POINTER(VARSTYPE), c_int)
        self.ffv = FFVTYPE(Space.iz.cs_findFreeVar)


    def search(self):
        return iz_bool(Space.iz.cs_search(self.array, self.size, self.ffv))
        
