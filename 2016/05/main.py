import sys
sys.path.append('../../')
from aoctools.aoc_functions import *
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque

import hashlib

def main():
    testing = 0

    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = ""
    ans2 = [None for _ in range(8)]

    line = ""
    with open(file) as fh:
        for line in fh:
            line = line.strip()
    
    hashlen = 8

    # part 1
    i = 0
    while len(ans1) < hashlen:
        r = hashlib.md5((line+str(i)).encode()).hexdigest()
        if r.startswith("00000"):
            ans1 += r[5]
        i += 1
    
    # part 2
    i = 0
    while None in ans2:
        r = hashlib.md5((line+str(i)).encode()).hexdigest()
        if r.startswith("00000"):
            if r[5] in "01234567":
                idx = int(r[5])
                if ans2[idx] is None:
                    ans2[idx] = r[6]
        i += 1
    ans2 = "".join(ans2)
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part1(lst):
    pass

def part2():
    pass

# ==================================================

if __name__ == "__main__":
    main()