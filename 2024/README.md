# AoC 2024
Another year, another Advent of Code! I repurposed the current repo so that I could use it for 2024 as well (originally, I was just going to create a new repo).

Once again, these were my solutions for [Advent of Code 2024](https://adventofcode.com/2024). I kept my solutions the way I had them when submitting the output, so some code may be messy (or quite inefficient, or specific to my input).

As of November 24, 2024, I am planning on working on the `aoctools` package again; specifically, the module that would allow me to automatically fetch the solutions from the internet (`aoc_web.py`).

## Usage
Simply go to every folder and run `python3 main.py`.

## Extras
### Hall of Shame
Yes, we're bringing this back from [2021](../2021/README.md#longest-runtimes-hall-of-shame-fame)! This time not with runtimes, but instead with notable things that I've had to debug for longer than I should.
1. [**Problem 3 Part 2**](./03/): I did not realize that instructions carry over into the next line (and the instructions never specified this!!!). The time between Part 1 and Part 2 was **14:06**.
2. [**Problem 4 Part 1**](./04/): I learned the hard way that negative indices are valid in Python. Part 1 took **19:03**.
2. [**Problem 12 Part 2**](./12/): I learned the very, very hard way that, while Python automatically sorts tuples by index 1 if you use `sort()` without a key (eg. if you use `sort()` on index 0), it will not automatically sort them by index 0 if you use `sort()` on index 1. The time between Part 1 and Part 2 was **01:44:45**.
