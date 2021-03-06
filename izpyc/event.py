from ctypes import *
from .space import Space
from .util import iz_bool
from .intutil import create_c_ptr_array
from .variable import Int


def known_bridge(val, index, tint, size, known):
    if known.fire(val, index):
        return 1
    else:
        return 0

class Known:
    def __init__(self, variables, callback):
        self.variables = variables
        self.callback = callback
        self.array = create_c_ptr_array(variables)

        KNOWNFUNC = CFUNCTYPE(c_byte, c_int, c_int, c_void_p, c_int, py_object)

        self.rc = iz_bool(Space.iz.cs_eventKnown(self.array, len(variables), KNOWNFUNC(known_bridge), py_object(self)))

    def fire(self, val, index):
        return self.callback(val, index, self.variables)

ev = None

def known(variables, callback):
    global ev
    ev = Known(variables, callback)
    # TODO: register ev to space
    return ev.rc
