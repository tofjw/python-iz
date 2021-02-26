import sys
sys.path.append("..")

import izpyc
import izpyc.constraint as C
from izpyc import Int
from izpyc.searcher import SimpleSearcher


# https://ja.wikipedia.org/wiki/%E6%95%B0%E7%8B%AC
x = 0
problem = [
    5,3,x, x,7,x, x,x,x,
    6,x,x, 1,9,5, x,x,x,
    x,9,8, x,x,x, x,6,x,

    8,x,x, x,6,x, x,x,3,
    4,x,x, 8,x,3, x,x,1,
    7,x,x, x,2,x, x,x,6,

    x,6,x, x,x,x, 2,8,x,
    x,x,x, 4,1,9, x,x,5,
    x,x,x, x,8,x, x,7,9,
    ]

for i in range(0, 9):
    for j in range(0, 9):
        v = problem[i * 9 + j]
        if v == 0:
            print("x", end=" ")
        else:
            print(v, end=" ")

        if (j + 1) % 3 == 0:
            print(" ", end="")

    if (i + 1) % 3 == 0:
        print("")
    print("")

print("---------------------------------------")


def cell_variable(c):
    if c == 0:
        return Int(1, 9)
    else:
        return Int(c)

with izpyc.space():
    variables = list(map(lambda c: cell_variable(c), problem))

    # row, col
    for i in range(0, 9):
        row = []
        col = []
        for j in range(0, 9):
            row.append(variables[i * 9 + j])
            col.append(variables[i + j * 9])

        C.all_neq(row)
        C.all_neq(col)

    # 3x3 block
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for x in range(i, i+3):
                for y in range(j, j+3):
                    block.append(variables[x * 9 + y])
            C.all_neq(block)

    rc = SimpleSearcher(variables).search()
    print("rc = ", rc)

    for i in range(0, 9):
        for j in range(0, 9):
            v = variables[i * 9 + j]
            print(v.value, end=" ")
            if (j + 1) % 3 == 0:
                print(" ", end="")

        if (i + 1) % 3 == 0:
            print("")
        print("")
