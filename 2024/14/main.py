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

    bots = []
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            line = raw_to_int(line)
            pos = tuple(line[:2])
            vel = tuple(line[2:])
            bots.append([pos, vel])

    width = 101
    height = 103

    for i in range(101*103):
        positions = []
        for bot in bots:
            positions.append(find_pos(width,height,bot[0],bot[1],i))
        if i == 100:
            ans1 = find_safe(width,height,positions)
        if len(set(positions)) == len(positions):
            ans2 = i
            grid_print(make_grid(width, height, positions))
            break

    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def find_pos(x, y, pos, vel, times):
    pos_x = (pos[0]+vel[0]*times) % x
    pos_y = (pos[1]+vel[1]*times) % y
    return (pos_x, pos_y)

def find_safe(x, y, positions):
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    for pos in positions:
        if (x%2!=0 and pos[0] == x//2) or (y%2!=0 and pos[1] == y//2):
            continue
        if pos[0] < x//2 and pos[1] < y//2:
            q1.append(pos)
        elif pos[0] >= x//2 and pos[1] < y//2:
            q2.append(pos)
        elif pos[0] < x//2 and pos[1] >= y//2:
            q3.append(pos)
        else:
            q4.append(pos)
    return len(q1)*len(q2)*len(q3)*len(q4)

def make_grid(x, y, positions):
    grid = []
    for i in range(y):
        inner = []
        for j in range(x):
            if (j,i) not in positions:
                inner.append('.')
            else:
                inner.append('#')
        grid.append(inner)
    return(grid)

# ==================================================

if __name__ == "__main__":
    main()
