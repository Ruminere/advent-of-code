import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
from collections import defaultdict, Counter, deque

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    instrs = {}
    vals = []
    mode = 0
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            # print(line)
            if len(line) == 0:
                break
                mode = 1
            elif mode == 0:
                line = line.strip("}")
                k = line[:line.find("{")]
                d = line[line.find("{")+1:].split(",")
                ins = [i.split(":") for i in d]
                instrs[k] = ins
            elif mode == 1:
                line = line.strip("{").strip("}").split(",")
                val = {l[0]:int(l[2:]) for l in line}
                vals.append(val)
    
    # print(instrs)
    # print("\n")
    # print("vals", vals)

    # for val in vals:
    #     ans1 += parse_instrs(instrs,val)
                
    for i in range(1,4001):
        print(i)
        for j in range(1,4001):
            for k in range(1,4001):
                for l in range(1,4001):
                    ans2 += 1 if parse_instrs(instrs, (i,j,k,l)) else 0
    
    # print("1:", ans1)
    print("2:", ans2)

# ==================================================

def parse_instrs(instrs, val):
    # x,m,a,s = val.values()
    x,m,a,s = val
    k = "in"
    # print(x,m,a,s)
    while k not in "AR":
        terms = instrs[k]
        for t in terms:
            if len(t) == 1:
                k = t[0]
            else:
                if eval(t[0]):
                    k = t[1]
                    break
    # return sum(val.values()) if k == "A" else 0
    return k == "A"


# ==================================================

main()