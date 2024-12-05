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

    instrs = defaultdict(list)
    upds = []
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                break
            line = list(map(int, line.split("|")))
            instrs[line[1]].append(line[0])
        for line in fh:
            line = list(map(int, line.strip().split(",")))
            upds.append(line)

    for upd in upds:
        if part1(instrs, upd) == (-1,-1):
            ans1 += upd[len(upd)//2]
        else:
            ans2 += part2(instrs, upd)

    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part1(instrs, upd):
    for i in rlen1(upd):
        for j in range(i+1,len(upd)):
            if upd[j] in instrs[upd[i]]:
                return i,j
    return -1,-1

def part2(instrs, upd):
    while True:
        i,j = part1(instrs,upd)
        if (i,j) == (-1,-1):
            break

        tmp = upd[i]
        upd[i] = upd[j]
        upd[j] = tmp
    
    return upd[len(upd)//2]

# ==================================================

if __name__ == "__main__":
    main()
