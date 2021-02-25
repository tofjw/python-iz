#
#
#

from ctypes import *


def setup(izlib):
    def x(f, argtype, restype):
        izlib.__getattr__(f).argtype = argtype
        izlib.__getattr__(f).restype = restype

    x("cs_Le", [c_void_p, c_void_p], c_char)
    x("cs_Lt", [c_void_p, c_void_p], c_char)
    x("cs_Ge", [c_void_p, c_void_p], c_char)
    x("cs_Gt", [c_void_p, c_void_p], c_char)
    x("cs_Eq", [c_void_p, c_void_p], c_char)
    x("cs_Neq", [c_void_p, c_void_p], c_char)

    x("cs_LE", [c_void_p, c_int], c_char)
    x("cs_LT", [c_void_p, c_int], c_char)
    x("cs_GE", [c_void_p, c_int], c_char)
    x("cs_GT", [c_void_p, c_int], c_char)
    x("cs_EQ", [c_void_p, c_int], c_char)
    x("cs_NEQ", [c_void_p, c_int], c_char)

    izlib.cs_createCSint.restype = c_void_p
    izlib.cs_getVersion.restype = c_char_p
    izlib.cs_getMin.argtypes = [c_void_p]
    izlib.cs_getMax.argtypes = [c_void_p]

    # izlib.cs_search.argtypes = [c_c]
    izlib.cs_search.restype = c_char
    izlib.cs_isFree.restype = c_char
    izlib.cs_isInstantiated.restype = c_char

    x("cs_ScalProd", [c_void_p, c_void_p, c_int], c_void_p)
1    
    # extern __izwindllexport IZBOOL cs_search(CSint **allvars, int nbVars, CSint* (*findFreeVar)(CSint **allvars, int nbVars));

