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
    grid = ftg(file, to_int=True)

    ans1 = part1(grid)
    ans2 = part2(grid)

    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part1(grid):
    heads = []
    for i in rlen(grid):
        for j in rlen(grid[0]):
            if grid[i][j] == 0:
                heads.append( (i,j) )

    tails = []
    
    for head in heads:
        closed = set()
        to_explore = deque([head])
        while to_explore:
            current = to_explore.pop()
            closed.add(current)
            if grid[current[0]][current[1]] == 9:
                tails.append(current)
                continue
            
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            for d in dirs:
                nbr = (current[0]+d[0], current[1]+d[1])
                if not in_bounds(grid, *nbr):
                    continue
                if nbr in closed:
                    continue
                if grid[nbr[0]][nbr[1]] != grid[current[0]][current[1]]+1:
                    continue
                to_explore.append(nbr)

    return len(tails)


def part2(grid):
    heads = []
    for i in rlen(grid):
        for j in rlen(grid[0]):
            if grid[i][j] == 0:
                heads.append( (i,j) )

    tails = []
    
    to_explore = deque(heads)
    while to_explore:
        current = to_explore.popleft()
        if grid[current[0]][current[1]] == 9:
            tails.append(current)
            continue
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for d in dirs:
            nbr = (current[0]+d[0], current[1]+d[1])
            if not in_bounds(grid, *nbr):
                continue
            if grid[nbr[0]][nbr[1]] != grid[current[0]][current[1]]+1:
                continue
            to_explore.append(nbr)

    return len(tails)


# ==================================================

if __name__ == "__main__":
    main()
