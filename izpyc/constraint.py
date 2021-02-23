from ctypes import *
from .space import Space
from .util import iz_bool
from .variable import Int

#
# common functions
#


def get_cs_int_ptr(v):
    if isinstance(v, Int):
        return v.p
    elif isinstance(v, int):
        cv = Int(v, v)
        return cv.p
    else:
        raise ValueError("operation is not defined for " + str(v))

    return None


def create_c_ptr_array(var_array):
    ptrs = map(get_cs_int_ptr, var_array)
    VARSTYPE = c_void_p * len(var_array)
    array = VARSTYPE()

    for i, p in enumerate(ptrs):
        array[i] = p

    return array


#
# constraints
#

def all_neq(variables):
    array = create_c_ptr_array(variables)
    Space.registered_array.append(array)
    return iz_bool(Space.iz.cs_AllNeq(array, len(variables)))
