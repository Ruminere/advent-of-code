# Problem 21
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 12524 | 4081 |
| Time | 08:11:53 | 09:28:52 |

Part 1 was straightforward. It took me a while to find my bug where I reset the queue of new coordinates when iterating over the current queue, but I got the correct answer shortly afterwards.

Part 2 was more interesting. Upon looking at the number, I instantly knew I would not be bashing that one out (especially since part 1 had taken around half a second), so I decided to see if I could find patterns within the way the steps worked. Within the actual input (not the testing data), the row and column the starting coordinate is in is completely blank, as is the outer ring of the starting grid. The grid is also a square, which simplified things. Additionally, `26501365 % 131` (the length of the grid) is 65, which is exactly the number of steps it takes to reach the edge of the first grid. I ate breakfast after this since it was ready, then decided to use polynomial interpolation for values `0`, `131`, and `131*2` courtesy of WolframAlpha. When that didn't work, I did the same thing for `65` and got the correct answer. (Had that not worked, I would've tried off-by-one answers.)