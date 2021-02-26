import sys
sys.path.append("..")

import izpyc
import izpyc.constraint as C
from izpyc import Int
from izpyc.searcher import SimpleSearcher


with izpyc.space():
    s = Int(0, 9)
    e = Int(0, 9)
    n = Int(0, 9)
    d = Int(0, 9)
    m = Int(0, 9)
    o = Int(0, 9)
    r = Int(0, 9)
    y = Int(0, 9)

    v1 = C.scal_prod([s, e, n, d], [1000, 100, 10, 1])
    v2 = C.scal_prod([m, o, r, e], [1000, 100, 10, 1])
    v3 = C.scal_prod([m, o, n, e, y], [10000, 1000, 100, 10, 1])
    v12 = C.scal_prod([v1, v2], [1, 1])

    C.all_neq([s, e, n, d, m, o, r, y])
    s != 0
    m != 0
    v3 == v12

    rc = SimpleSearcher([s, e, d, m, o, r, y]).search()
    print("rc = ", rc)

    print(s.value, e.value, n.value, d.value)
    print(m.value, o.value, r.value, e.value)
    print(m.value, o.value, n.value, e.value, y.value)
