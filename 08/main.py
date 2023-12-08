import sys, ast
sys.path.append('../')
from aoctools.aoc_functions import *

def main():
    filename = "actual"

    ans1 = 0
    ans2 = 0
    
    n = 0
    hands = []

    with open(filename + ".in") as fh:
        lines = fh.readlines()
        lines = [line.strip() for line in lines]
    directions = lines.pop(0)
    lines.pop(0)

    nodes = {}
    for line in lines:
        raw = line.split(" = ")
        raw1 = raw[1][1:-1]
        raw1 = raw1.split(", ")
        nodes[raw[0]] = tuple(raw1)

    currents = []
    for node in nodes.keys():
        if node[-1] == "A":
            currents.append(node)
    print(currents)

    all_steps = []
    for current in currents:
        steps = 0
        while True:
            dir_next = directions[steps % len(directions)]
            current = get_node(nodes, current, dir_next)
            steps += 1
            if current[-1] == "Z":
                break
        all_steps.append(steps)

    ans2 = math.lcm(*all_steps)

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def part_1(nodes):
    current = "AAA"
    steps = 0
    while True:
        dir_next = directions[steps % len(directions)]
        current = get_node(nodes, current, dir_next)
        steps += 1
        if current == "ZZZ":
            break
    return steps

def get_node(nodes, current, direction):
    return nodes[current][0] if direction == "L" else nodes[current][1]

# ==================================================

main()