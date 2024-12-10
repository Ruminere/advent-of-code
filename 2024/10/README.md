# Problem 10
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 3782 | 3596 |
| Time | 00:24:04 | 00:28:53 |

I skipped out on Days 6 and 7 since I had a ton of projects due on Dec 6. Then I started feeling really bad (I spent the majority of Dec 7 sleeping and Dec 8 mindlessly playing puzzle games), so I didn't do days 8 or 9 either. I'll look at both days when I have time this week. But on the upside, [I finished all three of my projects](../05/README.md), though—which I wasn't expecting, considering I procrastinated so much I was expecting to turn my Cache Lab project in late!

Part 1 took an embarrassingly long time to debug. My first answer was `1238`, which was wrong. I thought that I had read the instructions incorrectly *again*, so I reread it a lot and kept on getting `81` for the output. Then I started writing print statements and converted my BFS to DFS for easier debugging, and realized that my bug was the result of not keeping track of the coordinates that I'd already visited per trail head. After that, I quickly got `574`, which was correct.

Then came time for part 2. Before reading anything, I copied my stuff for part 1 and refactored it for part 2 so that the DFS would stop at the trail tail. I still got `36` for the test input, so I looked at the problem statement before realizing that the corresponding output was `81`. On a whim, I submitted `1238` for part 2, which was correct.

That was hilarious. I still don't know why my buggy part 1 BFS code worked for part 2, but that was hilarious.
