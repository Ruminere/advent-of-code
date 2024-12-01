import sys
sys.path.append('../../')
from aoctools.aoc_functions import *
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque

def main():
    testing = 0

    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    left = []
    right = []
    with open(file) as fh:
        for line in fh:
            line = line.strip().split()
            left.append(int(line[0]))
            right.append(int(line[1]))

    left.sort()
    right.sort()
    for i in rlen(left):
        ans1 += abs(left[i]-right[i])

    for l in left:
        times = 0
        for r in right:
            if l == r:
                times += 1
        ans2 += l*times
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part1():
    pass

def part2():
    pass

# ==================================================

if __name__ == "__main__":
    main()