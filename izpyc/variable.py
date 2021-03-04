#
# CSint wrapper
#

from ctypes import *
from .space import Space
from .util import iz_bool

class Int:
    def __init__(self, min_or_dom, max=None, ptr=None):
        if ptr is not None:
            self.p = ptr
        else:
            if hasattr(min_or_dom, "__iter__"):
                # min_or_dom is domain
                if max is not None:
                    raise RunTimeError("second arg is not needed")
                vals = list(min_or_dom)
                DOMTYPE = c_int * len(vals)
                array = DOMTYPE()
                for i, v in enumerate(vals):
                    array[i] = int(v)

                self.p = Space.iz.cs_createCSintFromDomain(array, len(vals))
            else:
                # min_or_dom is min
                if max is None:
                    c = int(min_or_dom)
                    self.p = Space.iz.cs_createCSint(c, c)
                else:
                    self.p = Space.iz.cs_createCSint(int(min_or_dom), int(max))
            
    @property
    def min(self):
        return Space.iz.cs_getMin(self.p)

    @property
    def max(self):
        return Space.iz.cs_getMax(self.p)

    @property
    def value(self):
        return Space.iz.cs_getValue(self.p)

    @property
    def is_instantiated(self):
        return iz_bool(Space.iz.cs_isInstantiated(self.p))

    @property
    def is_free(self):
        return iz_bool(Space.iz.cs_isFree(self.p))

    @property
    def nb_elements(self):
        return Space.iz.cs_getNbElements(self.p)


    def __str__(self):
        def end_value(v):
            max_value = self.max

            if v >= max_value:
                return max_value
            if self.is_in(v):
                cur = v
                while True:
                    if cur == max_value:
                        return max_value
                    if not self.is_in(cur+1):
                        return cur
                    cur = cur + 1
            else:
                return  Spae.iz.cs_getNextValue(self, v);

        if self.is_instantiated:
            return str(self.min)

        min_value = self.min
        max_value = self.max
        if max_value - min_value + 1 == self.nb_elements:
            return "{" + "{}..{}".format(min_value, max_value) + "}"
        
        seg = []
        cur = min_value
        end = None

        while True:
            end = end_value(cur)
            if end == cur:
                seg.append(str(cur))
            else:
                seg.append("{}..{}".format(cur, end))

            if end >= max_value:
                break

            cur = Space.iz.cs_getNextValue(self.p, end)

        return "{" + ", ".join(seg) + "}"


    def is_in(self, val):
        return iz_bool(Space.iz.cs_isIn(self.p, val))
    

    def iz_cmp_op(self, other, izfunc, izfunc_const):
        if isinstance(other, Int):
            return iz_bool(izfunc(self.p, other.p))
        elif isinstance(other, int):
            return iz_bool(izfunc_const(self.p, other))
        else:
            raise ValueError("operation is not defined for " + str(other))
        

    def __eq__(self, other):
        return self.iz_cmp_op(other, Space.iz.cs_Eq, Space.iz.cs_EQ)


    def __ne__(self, other):
        return self.iz_cmp_op(other, Space.iz.cs_Neq, Space.iz.cs_NEQ)

    
    def __le__(self, other):
        return self.iz_cmp_op(other, Space.iz.cs_Le, Space.iz.cs_LE)


    def __lt__(self, other):
        return self.iz_cmp_op(other, Space.iz.cs_Lt, Space.iz.cs_LT)


    def __ge__(self, other):
        return self.iz_cmp_op(other, Space.iz.cs_Ge, Space.iz.cs_GE)


    def __gt__(self, other):
        return self.iz_cmp_op(other, Space.iz.cs_Gt, Space.iz.cs_GT)


    def __add__(self, other):
        if isinstance(other, Int):
            return Int(0, ptr=Space.iz.cs_Add(self.p, other.p))
        elif isinstance(other, int):
            v = Int(other, other)
            return Int(0, ptr=Space.iz.cs_Add(self.p, v.p))
        else:
            raise ValueError("operation is not defined for " + str(other))

    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        if isinstance(other, Int):
            return Int(0, ptr=Space.iz.cs_Sub(self.p, other.p))
        elif isinstance(other, int):
            v = Int(other, other)
            return Int(0, ptr=Space.iz.cs_Sub(self.p, v.p))
        else:
            raise ValueError("operation is not defined for " + str(other))

    def __rsub__(self, other):
        if isinstance(other, Int):
            return Int(0, ptr=Space.iz.cs_Sub(other.p, self.p))
        elif isinstance(other, int):
            v = Int(other, other)
            return Int(0, ptr=Space.iz.cs_Sub(v.p, self.p))
        else:
            raise ValueError("operation is not defined for " + str(other))

    def __mul__(self, other):
        if isinstance(other, Int):
            return Int(0, ptr=Space.iz.cs_Mul(self.p, other.p))
        elif isinstance(other, int):
            v = Int(other, other)
            return Int(0, ptr=Space.iz.cs_Mul(self.p, v.p))
        else:
            raise ValueError("operation is not defined for " + str(other))

    def __rmul__(self, other):
        return self.__mul__(other)
