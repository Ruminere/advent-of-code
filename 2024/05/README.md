# Problem 5
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 2057 | 1506 |
| Time | 00:12:50 | 00:19:45 |

I have 3 assignments that are due at 23:59 on Friday (it is Wednesday), and I have finished exactly 0 of those 3 assignments. Yet here I am, writing this rant.

Due to the multitude of assignments that I have to complete, I was about to dip when I saw the input; I still had "trauma" from doing [2023 Day 5](../../2023/05/) all night. But I'm a completionist, so I decided to stick to it anyway.

I changed the way I did thing three times over; twice during part 1, and once during part 2. I was using a dictionary for the lines with pipe characters, so at first I had `instrs[line[1]].append(line[0])`; then I scrapped that, changed it to `instrs[line[0]].append(line[1])`, and reversed the order of the line. Then during part 2, I changed it once *again* so that it was `instrs[line[1]].append(line[0])` and so the line order wasn't reversed, because it was easier to do part 2 that way.
