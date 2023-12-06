import math, re
import itertools
import os, sys

# VARIABLES

directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "NW": (-1,-1),
    "NE": (1,-1),
    "SW": (-1,1),
    "SE": (1,1),
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "^": (-1, 0),
    "V": (1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

dirs = directions

# GRID FUNCTIONS

def grid_in_bounds(grid: list, row: int, col: int):
    '''
    Returns a boolean value indicating whether the desired grid coordinate is in bounds.
    '''
    dim = (len(grid), len(grid[0]))
    return row >= 0 and row < dim[0] and col >= 0 and col < dim[1]
in_bounds = grid_in_bounds

def grid_coord_neighobors(grid: list, row: int, col: int):
    '''
    Takes a grid coordinate and returns the surrounding coordinates.
    '''
    if not in_bounds(grid, row, col):
        raise ValueError("grid coordinate is out of bounds")

    ans = []
    for coord in itertools.islice(dirs.values(),8):
        row_new = row + coord[0]
        col_new = col + coord[1]
        if in_bounds(grid, row_new, col_new):
            ans.append( (row_new, col_new) )
    return ans
coord_neighbors = grid_coord_neighobors

def grid_neighbors(grid: list, row: int, col: int):
    '''
    Returns a list of all neighboring values surrounding the element with the given coordinates.
    '''
    return [grid[coord[0]][coord[1]] for coord in coord_neighbors(grid, row, col)]

def file_to_grid(filename: str, start=0, to_int=True):
    '''
    Reads a file and converts it to a grid starting from the starting line. Converts to integers if the setting is on.
    '''
    grid = []
    with open(filename + ".in") as fh:
        for line in fh:
            row = list(line.strip())
            if to_int:
                row = [int(val) for val in row]
            grid.append(row)
    return grid

def grid_print(grid: list):
    '''
    Prints a grid of characters.
    '''
    for row in grid:
        rowstr = ""
        for val in row:
            rowstr += str(val)
        print(rowstr)

# STRING TO NUMBER COMPREHENSION

def raw_to_int(raw: str, neg=True):
    '''
    Returns a list of all integers in a string. Includes negative symbols by default.
    '''
    to_find = r"-?\d+" if neg else r"\d+"
    return [int(n) for n in re.findall(to_find, raw.strip())]

def raw_to_int(raw: str, neg=True):
    '''
    Returns a list of all digits in a string. Includes negative symbols by default.
    '''
    to_find = r"-?\d" if neg else r"\d"
    return [int(n) for n in re.findall(to_find, raw.strip())]

def raw_to_float(raw: str, neg=True):
    '''
    Returns a list of all decimals in a string. Includes negative symbols by default.
    '''
    to_find = r"-?\d*\.?\d+" if neg else r"\d*\.?\d+"
    return [float(n) for n in re.findall(to_find, raw.strip())]