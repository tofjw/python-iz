#
# CSint wrapper
#

from .space import Space
from .util import iz_bool

class Int:
    def __init__(self, min, max=None, ptr=None):
        if ptr is not None:
            self.p = ptr
        else:
            if max is None:
                self.p = Space.iz.cs_createCSint(min, min)
            else:
                self.p = Space.iz.cs_createCSint(min, max)
            
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
            print("end value of ", cur, " is ", end)
            if end == cur:
                seg.append(str(cur))
            else:
                print("end = ", end)
                seg.append("{}..{}".format(cur, end))

            if end >= max_value:
                break

            cur = Space.iz.cs_getNextValue(self.p, end)

        return "{" + ", ".join(seg) + "}"


    def is_in(self, val):
        return iz_bool(Space.iz.cs_isIn(self.p, val))
    

    def __eq__(self, other):
        if isinstance(other, Int):
            return iz_bool(Space.iz.cs_Eq(self.p, other.p))
        elif isinstance(other, int):
            return iz_bool(Space.iz.cs_EQ(self.p, other))
        else:
            raise ValueError("operation is not defined for " + str(other))

    def __ne__(self, other):
        if isinstance(other, Int):
            return iz_bool(Space.iz.cs_Neq(self.p, other.p))
        elif isinstance(other, int):
            return iz_bool(Space.iz.cs_NEQ(self.p, other))
        else:
            raise ValueError("operation is not defined for " + str(other))
    
    def __le__(self, other):
        if isinstance(other, Int):
            return iz_bool(Space.iz.cs_Le(self.p, other.p))
        elif isinstance(other, int):
            return iz_bool(Space.iz.cs_LE(self.p, other))
        else:
            raise ValueError("operation is not defined for " + str(other))

    def __lt__(self, other):
        if isinstance(other, Int):
            return iz_bool(Space.iz.cs_Lt(self.p, other.p))
        elif isinstance(other, int):
            return iz_bool(Space.iz.cs_LT(self.p, other))
        else:
            raise ValueError("operation is not defined for " + str(other))

    def __ge__(self, other):
        if isinstance(other, Int):
            return iz_bool(Space.iz.cs_Ge(self.p, other.p))
        elif isinstance(other, int):
            return iz_bool(Space.iz.cs_GE(self.p, other))
        else:
            raise ValueError("operation is not defined for " + str(other))

    def __gt__(self, other):
        if isinstance(other, Int):
            return iz_bool(Space.iz.cs_Gt(self.p, other.p))
        elif isinstance(other, int):
            return iz_bool(Space.iz.cs_GT(self.p, other))
        else:
            raise ValueError("operation is not defined for " + str(other))
