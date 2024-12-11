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

    line = ""
    with open(file) as fh:
        for line in fh:
            line = line.strip().split()

    for i in range(75):
        print(i)
        line = part1(line)
    ans1 = len(line)

    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part1(line:list):
    final = []
    # 0 -> 1
    for l in line:
        if l == '0':
            final.append('1')
        elif len(l) % 2 == 0:
            final.append(str(int(l[:len(l)//2])))
            final.append(str(int(l[len(l)//2:])))
        else:
            final.append(str(int(l)*2024))

    return final



def part2(line):
    pass

# ==================================================

if __name__ == "__main__":
    main()
