# Problem 3
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 1724 | 3488 |
| Time | 00:05:27 | 00:19:33 |

A simple regex problem, so part 1 wasn't too bad.

Part 2, on the other hand, took forever. Look at `bruh.txt`; I was looking through every line to try to figure out what went wrong with my code, except that the bug was that I didn't let instructions carry over from line to line. The instructions don't even say the `do()` and `don't()` flags carry over. It took me around 14 literal minutes of debugging before I realized my mistake.

Only day 3 and already looking through print statements to find nonexistent bugs!

P.S. The only `re` command I know in Python is `re.findall()`.

P.P.S. I did this question during a take-home exam. I'm pretty sure I did awfully on it, but oh well, the lowest exam score gets dropped anyway.
