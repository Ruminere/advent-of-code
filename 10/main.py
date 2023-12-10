import sys
sys.path.append('../')
from aoctools.aoc_functions import *

'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''

def main():
    testing = 1
    filename = "actual" if not testing else "test"

    ans1 = 0
    ans2 = 0

    grid = ftg(filename)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i,j)
                break
    
    raw = bfs(grid, start)
    ans1 = raw[0]

    dist = raw[1]
    clean_grid(grid, dist)
    grid_print(grid)

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

dirs = {"|": [(-1,0),(1,0)],
        "-": [(0,-1),(0,1)],
        "L": [(-1,0),(0,1)],
        "J": [(-1,0),(0,-1)],
        "7": [(1,0),(0,-1)],
        "F": [(1,0),(0,1)],
        ".": [],
        "S": [(-1,0),(1,0),(0,-1),(0,1)]}

def gcn(grid: list, row: int, col: int, sign: str):
    '''
    Takes a grid coordinate and returns the surrounding coordinates.
    '''
    if not in_bounds(grid, row, col):
        raise ValueError("grid coordinate is out of bounds")

    ans = []
    
    d = {(-1,0):(1,0),
         (1,0):(-1,0),
         (0,1):(0,-1),
         (0,-1):(0,1)}
    
    # print("current", (row,col), dirs[sign])
    for coord in d.keys():
        
        if coord not in dirs[sign]:
            continue
        row_new = row + coord[0]
        col_new = col + coord[1]
        if not in_bounds(grid, row_new, col_new):
            # print("oob")
            continue
        sign_new = grid[row_new][col_new]
        # print((row_new, col_new), dirs[sign_new])
        if d[coord] in dirs[sign_new]:
            ans.append( (row_new, col_new) )
    return ans

def bfs(grid, start):
    '''
    start is a grid coordinate
    '''
    to_explore = []
    dist = {}
    to_explore.append(start)
    dist[start] = 0
    while len(to_explore) > 0:
        current = to_explore.pop(0)
        nbrs = gcn(grid, current[0], current[1], grid[current[0]][current[1]])
        # print("current", current)
        # print("nbrs", nbrs)
        # print("explore", to_explore)
        # print("dist", dist)
        for nbr in nbrs:
            nbr_dist = dist[current] + 1
            if nbr not in dist.keys():
                dist[nbr] = nbr_dist
                to_explore.append(nbr)
            if dist[nbr] > nbr_dist:
                dist[nbr] = nbr_dist
    high = -float("inf")
    for val in dist.values():
        if val > high:
            high = val
    return high, dist

def clean_grid(grid, dist):
    '''
    Modifies grid.
    '''
    loop = dist.keys()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) not in dist.keys():
                grid[i][j] = "."

# ==================================================

main()