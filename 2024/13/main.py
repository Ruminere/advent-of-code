import sys
sys.path.append('../../')
from aoctools.aoc_functions import *
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque
import re
import sympy as sp

def main():
    testing = 0

    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    with open(file) as fh:
        while fh:
            a = raw_to_int(fh.readline())
            if not a:
                break
            b = raw_to_int(fh.readline())
            t = raw_to_int(fh.readline())
            fh.readline()

            t2 = [i+10000000000000 for i in t]

            r = combos(a,b,t)
            r2 = combos(a,b,t2)
            if r != (-1,-1):
                ans1 += 3*r[0] + r[1]
            if r2 != (-1,-1):
                ans2 += 3*r2[0] + r2[1]

    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def combos(a_l,b_l,t_l):
    a_x, a_y = a_l
    b_x, b_y = b_l
    t_x, t_y = t_l

    a, b = sp.symbols('a b')
    x_eq = sp.Eq(a_x*a + b_x*b, t_x)
    y_eq = sp.Eq(a_y*a + b_y*b, t_y)
    
    s = sp.solve((x_eq, y_eq), (a, b))
    s = tuple(s.values())
    if any(not s[i].is_integer for i in rlen(s)):
        return (-1,-1)
    return s


def part2(line):
    pass

# ==================================================

if __name__ == "__main__":
    main()
