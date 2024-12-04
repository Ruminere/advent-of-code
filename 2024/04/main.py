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
    # with open(file) as fh:
    #     for line in fh:
    #         line = line.strip()
            # line = [int(i) for i in line]
            # lines.append(line)
            # ans1 += part1(line)
            # ans2 += part2(line)

    grid = ftg(filename)
    ans1 = part1(grid)
    ans2 = part2(grid)

    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

HORIZONTAL=0
VERTICAL=1
DIAGONAL1=2
DIAGONAL2=3

def part1(grid):
    ans = 0
    for i in rlen(grid):
        for j in rlen(grid[0]):
            if grid[i][j] in "XS":
                for a in range(4):
                    ans += search1(grid,i,j,a)
    return ans

def search1(grid, i, j, direction):
    s = ""

    try:
        if direction == HORIZONTAL:
            for k in range(0,4):
                s += grid[i][j+k]
        elif direction == VERTICAL:
            for k in range(0,4):
                s += grid[i+k][j]
        elif direction == DIAGONAL1:
            for k in range(0,4):
                s += grid[i+k][j+k]
        elif direction == DIAGONAL2:
            for k in range(0,4):
                if i-k < 0:
                    return 0
                s += grid[i-k][j+k]
    except:
        return 0
    
    if s == "XMAS" or s == "SAMX":
        return 1
    
    return 0

def part2(grid):
    ans = 0
    for i in rlen(grid):
        for j in rlen(grid[0]):
            if grid[i][j] in "A":
                ans += search2(grid,i,j)
    return ans

def search2(grid, i, j):
    try:
        tl = grid[i-1][j-1]
        bl = grid[i+1][j-1]
        tr = grid[i-1][j+1]
        br = grid[i+1][j+1]
    except:
        return 0
    
    if (tl == "M" and br == "S") or (tl == "S" and br == "M"):
        if (bl == "M" and tr == "S") or (bl == "S" and tr == "M"):
            return 1
    return 0

# ==================================================

if __name__ == "__main__":
    main()
