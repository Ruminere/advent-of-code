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

    stones = defaultdict(int)
    for s in line:
        stones[int(s)] += 1

    for i in range(25):
        stones = part1(stones)
    ans1 = sum(v for v in stones.values())
    for i in range(50):
        stones = part1(stones)
    ans2 = sum(v for v in stones.values())

    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part1(stones):
    stones_new = defaultdict(int)
    for k, v in stones.items():
        if k == 0:
            stones_new[1] += v
        elif len(str(k)) % 2 == 0:
            k_str = str(k)
            left = int(k_str[:len(k_str)//2])
            right = int(k_str[len(k_str)//2:])
            stones_new[left] += v
            stones_new[right] += v
        else:
            stones_new[k*2024] += v

    return stones_new


def part2(line):
    pass

# ==================================================

if __name__ == "__main__":
    main()
