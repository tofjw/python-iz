#
#
#

from ctypes import *


def setup(izlib):
    def x(f, argtype, restype):
        izlib.__getattr__(f).argtype = argtype
        izlib.__getattr__(f).restype = restype

    izbool_t = c_char
    
    x("cs_Le", [c_void_p, c_void_p], izbool_t)
    x("cs_Lt", [c_void_p, c_void_p], izbool_t)
    x("cs_Ge", [c_void_p, c_void_p], izbool_t)
    x("cs_Gt", [c_void_p, c_void_p], izbool_t)
    x("cs_Eq", [c_void_p, c_void_p], izbool_t)
    x("cs_Neq", [c_void_p, c_void_p], izbool_t)

    x("cs_LE", [c_void_p, c_int], izbool_t)
    x("cs_LT", [c_void_p, c_int], izbool_t)
    x("cs_GE", [c_void_p, c_int], izbool_t)
    x("cs_GT", [c_void_p, c_int], izbool_t)
    x("cs_EQ", [c_void_p, c_int], izbool_t)
    x("cs_NEQ", [c_void_p, c_int], izbool_t)

    x("cs_isIn", [c_void_p, c_int], izbool_t)
    x("cs_isFree", [c_void_p], izbool_t)
    x("cs_isInstantiated", [c_void_p], izbool_t)

    izlib.cs_createCSint.restype = c_void_p
    izlib.cs_getVersion.restype = c_char_p
    izlib.cs_getMin.argtypes = [c_void_p]
    izlib.cs_getMax.argtypes = [c_void_p]

    # izlib.cs_search.argtypes = [c_c]
    izlib.cs_search.restype = izbool_t

    x("cs_ScalProd", [c_void_p, c_void_p, c_int], c_void_p)
1    
    # extern __izwindllexport IZBOOL cs_search(CSint **allvars, int nbVars, CSint* (*findFreeVar)(CSint **allvars, int nbVars));

