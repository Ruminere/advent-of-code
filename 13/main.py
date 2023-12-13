import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as its

def main():
    testing = 0
    filename = "actual" if not testing else "test"

    ans1 = 0
    ans2 = 0

    grids = []
    grid = []
    lines = open(filename + ".in").readlines()
    lines.append("")
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            grids.append(grid.copy())
            grid.clear()
        else:
            grid.append(list(line))

    # print(row_flipped(grids[1],3))

    for grid in grids:
        # raw1 = find_flipped(grid)
        # print(raw1)
        # if raw1[0] == -1:
        #     ans1 += raw1[1]+1
        # else:
        #     ans1 += 100 * (raw1[0]+1)

        raw2 = find_flipped_fix(grid)
        print(raw2)
        if raw2[0] == -1:
            ans1 += raw2[1]+1
        else:
            ans1 += 100 * (raw2[0]+1)
        
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def find_flipped(grid):
    # grid_print(grid)
    for i in range(len(grid)-1):
        print("check row", i)
        if row_flipped(grid, i):
            return [i,-1]
    for i in range(len(grid[0])-1):
        print("check col", i)
        if col_flipped(grid,i):
            return [-1,i]
    return [-1,-1]

def col_flipped(grid, col):
    '''
    col / col+1
    '''
    dim = len(grid[0])
    i = 0
    while col-i >= 0 and col+1+i < dim:
        print(col-i, col+i+1)
        one = [row[col-i] for row in grid]
        two = [row[col+1+i] for row in grid]
        if not all(one[i] == two[i] for i in rlen(one)):
            return False
        i += 1
    return True

def row_flipped(grid, row):
    return col_flipped(numpy.transpose(grid), row)

def find_flipped_fix(grid):
    grid_print(grid)
    for i in range(len(grid)-1):
        print("check row", i)
        if row_flipped_fix(grid, i):
            return [i,-1]
    for i in range(len(grid[0])-1):
        print("check col", i)
        if col_flipped_fix(grid,i):
            return [-1,i]
    return [-1,-1]

def col_flipped_fix(grid, col):
    '''
    col / col+1
    '''
    dim = len(grid[0])
    i = 0
    count = 0
    while col-i >= 0 and col+1+i < dim:
        print(col-i, col+i+1)
        one = [row[col-i] for row in grid]
        two = [row[col+1+i] for row in grid]
        print(one)
        print(two)
        for j in rlen(one):
            if one[j] != two[j]:
                count += 1
        i += 1
    print(count)
    return count == 1

def row_flipped_fix(grid, row):
    return col_flipped_fix(numpy.transpose(grid), row)

# ==================================================

main()