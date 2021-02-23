from ctypes import *
from .util import iz_bool

class Space:
    iz = None
    registered_array = []
    
    def __init__(self, izlib):
        self.izlib = izlib
        return

    def __enter__(self):
        self.izlib.cs_init()
        Space.iz = self.izlib
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.izlib.cs_end()
        Space.iz = None
