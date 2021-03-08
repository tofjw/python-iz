#
#
#

from ctypes import *


def setup(izlib):
    def x(f, argtypes, restype):
        fa = getattr(izlib, f)
        setattr(fa, "argtypes", argtypes)
        setattr(fa, "restype", restype)


    def var_prop_int(f):
        x(f, [c_void_p], c_int)


    izbool_t = c_char


    def var_prop_bool(f):
        x(f, [c_void_p], izbool_t)
    

    var_prop_int("cs_getMin")
    var_prop_int("cs_getMax")
    var_prop_int("cs_getNbElements")
    var_prop_int("cs_getValue")

    var_prop_bool("cs_isInstantiated")
    var_prop_bool("cs_isFree")

    x("cs_getNextValue", [c_void_p, c_int], c_int)
    x("cs_getPreviousValue", [c_void_p, c_int], c_int)
    
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

    x("cs_Add", [c_void_p, c_void_p], c_void_p)
    x("cs_Sub", [c_void_p, c_void_p], c_void_p)
    x("cs_Mul", [c_void_p, c_void_p], c_void_p)

    x("cs_ScalProd", [c_void_p, c_void_p, c_int], c_void_p)
    x("cs_Sigma", [c_void_p, c_int], c_void_p)
    x("cs_AllNeq", [c_void_p, c_int], c_void_p)

    x("cs_Abs", [c_void_p], c_void_p)

    x("cs_Min", [c_void_p, c_int], c_void_p)
    x("cs_Max", [c_void_p, c_int], c_void_p)
    
    x("cs_saveContext", [], c_int)
    x("cs_restoreContextUntil", [c_int], None)
    x("cs_forgetSaveContextUntil", [c_int], None)

    x("cs_createCSint", [c_int, c_int], c_void_p)
    x("cs_createCSintFromDomain", [c_void_p, c_int], c_void_p)

    x("cs_findFreeVar", [c_void_p, c_int], c_void_p)
    x("cs_search", [c_void_p, c_int, c_void_p], izbool_t)

    x("cs_eventKnown", [c_void_p, c_int, c_void_p, c_void_p], izbool_t)
    
    x("cs_init", [], c_void_p)
    x("cs_end", [], c_void_p)
    x("cs_getVersion", [], c_char_p)

    
    # extern __izwindllexport IZBOOL cs_search(CSint **allvars, int nbVars, CSint* (*findFreeVar)(CSint **allvars, int nbVars));

