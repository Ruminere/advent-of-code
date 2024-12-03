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

    # lines = []
    with open(file) as fh:
        lines = fh.read().strip()
        ans1 += part1(lines)
        ans2 += part2(lines)
        # for line in fh:
            # line = line.strip()
            # line = [int(i) for i in line]
            # lines.append(line)
            
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part1(line):
    r = r"mul\((\d+),(\d+)\)"
    ms = re.findall(r,line)
    total = 0
    for m in ms:
        num1, num2 = int(m[0]), int(m[1])
        total += num1*num2
    return total

def part2(line):
    r = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    do = True
    ms = re.findall(r,line)
    total = 0
    for m in ms:
        if do:
            if m == "don't()":
                do = False
            elif "mul" in m:
                t = r"mul\((\d+),(\d+)\)"
                ts = re.findall(t,m)
                for u in ts:
                    num1, num2 = int(u[0]), int(u[1])
                    total += num1*num2
        else:
            if m == "do()":
                do = True
    return total

# ==================================================

if __name__ == "__main__":
    main()
