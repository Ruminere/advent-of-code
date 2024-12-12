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
    #         line = line.split()
    #         line = [int(i) for i in line]
    #         lines.append(line)
            # ans1 += part1(line)
            # ans2 += part2(line)
    grid = ftg(file)
    ans1, ans2 = solve(grid)

    print("ENSURE THAT THIS IS NOT THE TEST INPUT")
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def solve(grid):
    ans1 = 0
    ans2 = 0

    plots = defaultdict(list)
    plots_dupl = defaultdict(int)
    for i in rlen(grid):
        for j in rlen(grid[0]):
            plot = grid[i][j]+str(plots_dupl[grid[i][j]])
            current = (i,j)
            if not any(current in plots[grid[i][j]+str(p)] for p in range(plots_dupl[grid[i][j]])):
                plots_dupl[grid[i][j]] = plots_dupl[grid[i][j]] + 1
                plots[plot] = bfs(grid,current)
    print(plots)
    for plot, coords in plots.items():
        area = len(coords)
        perimeter = find_perimeter(grid, coords)
        edges = find_edges(grid, coords)
        ans1 += area*perimeter
        ans2 += area*edges
        print(plot,area,edges)
    
    return ans1, ans2

def bfs(grid, start):
    closed = set()
    to_explore = deque([start])
    while to_explore:
        current = to_explore.pop()
        closed.add(current)
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for d in dirs:
            nbr = (current[0]+d[0], current[1]+d[1])
            if not in_bounds(grid, *nbr):
                continue
            if nbr in closed:
                continue
            if grid[nbr[0]][nbr[1]] != grid[start[0]][start[1]]:
                continue
            to_explore.append(nbr)

    return list(closed)

def find_perimeter(grid, coords):
    perimeter = 0
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for current in coords:
        for d in dirs:
            nbr = (current[0]+d[0], current[1]+d[1])
            if nbr not in coords:
                perimeter += 1
    return perimeter

def find_edges(grid, coords):
    edges = 0
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    edges_raw = {d:[] for d in dirs}
    for current in coords:
        for d in dirs:
            nbr = (current[0]+d[0], current[1]+d[1])
            if nbr not in coords:
                edges_raw[d].append(nbr)
    for d in [(-1,0),(1,0)]:
        edge_raw = sorted(edges_raw[d])
        # print(d,edge_raw)
        for i in rlen1(edge_raw):
            c0 = edge_raw[i]
            c1 = edge_raw[i+1]
            if c0[0] != c1[0] or abs(c0[1]-c1[1]) != 1:
                edges += 1
        # print(edges)
    for d in [(0,-1),(0,1)]:
        edge_raw = sorted(edges_raw[d])
        edge_raw.sort(key=lambda i:i[1])
        print(d,edge_raw)
        c = 0
        for i in rlen1(edge_raw):
            c0 = edge_raw[i]
            c1 = edge_raw[i+1]
            if c0[1] != c1[1] or abs(c0[0]-c1[0]) != 1:
                c += 1
                edges += 1
        print(c)
        
        # print(edges)
        
    return edges+4

# ==================================================

if __name__ == "__main__":
    main()
