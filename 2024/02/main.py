import sys
sys.path.append('../../')
from aoctools.aoc_functions import *
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque

def main():
    testing = 0

    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    lines = []
    with open(file) as fh:
        for line in fh:
            line = line.strip().split()
            line = [int(i) for i in line]
            lines.append(line)
    
    failed = []
    for line in lines:
        if not part1(line):
            ans1 += 1
        else:
            failed.append(line)
        
    ans2 = ans1
    for line in failed:
        for i in range(len(line)):
            newline = line[:i] + line[i+1:]
            if not part1(newline):
                ans2 += 1
                break

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part1(line):
    if abs(line[1]-line[0]) == 0:
        return True
    
    multiplier = (line[1]-line[0])/abs(line[1]-line[0])
    fail = False
    for i in range(len(line)-1):
        if abs(line[i]-line[i+1]) not in [1,2,3]:
            fail = True
            break
        if (line[i+1]-line[i])/abs(line[i]-line[i+1]) != multiplier:
            fail = True
            break
    return fail

# ==================================================

if __name__ == "__main__":
    main()