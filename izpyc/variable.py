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
        print(Space.iz.cs_isInstantiated(self.p))
        return iz_bool(Space.iz.cs_isInstantiated(self.p))

    @property
    def is_free(self):
        return iz_bool(Space.iz.cs_isFree(self.p))

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
