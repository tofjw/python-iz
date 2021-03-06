from ctypes import *
from .space import Space
from .util import iz_bool
from .intutil import create_c_ptr_array
from .variable import Int

#
# common functions
#

def create_const_array(const_array):
    CTYPE = c_int * len(const_array)
    array = CTYPE()

    for i, c in enumerate(const_array):
        array[i] = c

    return array

#
# constraints
#

def all_neq(variables):
    array = create_c_ptr_array(variables)
    Space.registered_array.append(array)
    return iz_bool(Space.iz.cs_AllNeq(array, len(variables)))


def scal_prod(variables, coeffs):
    varray = create_c_ptr_array(variables)
    carray = create_const_array(coeffs)
    Space.registered_array.append(varray)
    Space.registered_array.append(carray)
    return Int(0, ptr=Space.iz.cs_ScalProd(varray, carray, len(variables)))


def sigma(variables):
    varray = create_c_ptr_array(variables)
    Space.registered_array.append(varray)
    return Int(0, ptr=Space.iz.cs_Sigma(varray, len(variables)))


def abs(v):
    return Int(0, ptr=Space.iz.cs_Abs(v.p))


def min(variables):
    varray = create_c_ptr_array(variables)
    Space.registered_array.append(varray)
    return Int(0, ptr=Space.iz.cs_Min(varray, len(variables)))


def max(variables):
    varray = create_c_ptr_array(variables)
    Space.registered_array.append(varray)
    return Int(0, ptr=Space.iz.cs_Max(varray, len(variables)))
