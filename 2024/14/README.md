# Problem 14
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 2049 | 555 |
| Time | 00:20:10 | 00:27:19 |

Part 1 took too long to debug. I had an extra `x%2!=0` case in case the grid sizes became even, but I had it as `x%2==0` at first. Then I used the test input, got the right answer for the input, then debugged for a while longer since it didn't work on the real thing... until I realized that I had put the test input sizes (11,7) for the real thing (101,103).

For part 2, I misread the problem and assumed that I would literally see an egg on the screen. Bracing myself, I actually coded the grid out. Then I printed every iteration in `range(101*103)` (101 and 103 are both prime, so I couldn't use divide by the GCD)... then got tired of searching for the egg after around `i=663`. I then wondered if the easter egg would appear when all the robots were at different points (if not I was planning to start searching for multiple `#` characters in a row; I used `#` if there was a robot occupying the space), and my guess was correct—except I saw a tree instead.
