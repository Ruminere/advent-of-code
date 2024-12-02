# Problem 2
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 1827 | 1293 |
| Time | 00:08:22 | 00:12:32 |

This problem would not load at first; I got a 500 error. I reloaded, then after a minute I got a 504 error for the problem description (my input loaded at this point). This ruined my chances of getting on the leaderboard (not that I was getting on there in the first place, but still).

I choked multiple times for part 1; I first did `line[i]-line[i+1]` instead of `line[i+1]-line[i]` as intended (see lines 51 and 54; I kept the ones within the `abs`), so everything failed (I was checking for whether the numbers stayed consistently increasing or decreasing). That cost me more time than I'd like to admit.

I used `part1` as the function name since my template has `part1` and `part2` as default function names. It returns `True` if the line fails, which is a bit counterintuitive since we'd expect it to return `True` if the line passes, but hey, I was trying to go fast.
