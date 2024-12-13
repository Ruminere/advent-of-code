import sys
sys.path.append('../../')
from aoctools.aoc_functions import *
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque
import re

def main():
    testing = 0

    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    lines = []
    with open(file) as fh:
        while fh:
            a = raw_to_int(fh.readline())
            if not a:
                break
            b = raw_to_int(fh.readline())
            t = raw_to_int(fh.readline())
            
            fh.readline()
            r = combos(a,b,t)
            if r != (-1,-1):
                ans1 += 3*r[0] + r[1]


    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def combos(a,b,t):
    lowest = (float('inf'),float('inf'))
    a_x, a_y = a
    b_x, b_y = b
    t_x, t_y = t

    x_cur = 0
    y_cur = 0
    for a_pressed in range(101):
        for b_pressed in range(101):
            x_cur = a_x*a_pressed + b_x*b_pressed
            y_cur = a_y*a_pressed + b_y*b_pressed
            if x_cur > t_x or y_cur > t_y:
                break
            if x_cur == t_x and y_cur == t_y:
                if lowest[0]*3+lowest[1] > a_pressed*3 + b_pressed:
                    lowest = (a_pressed,b_pressed)
                    return lowest
    
    return (-1,-1)


def part2(line):
    pass

# ==================================================

if __name__ == "__main__":
    main()
