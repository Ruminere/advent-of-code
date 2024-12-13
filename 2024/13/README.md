# Problem 13
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 1930 | 1736 |
| Time | 00:19:47 | 00:42:01 |

My first reaction:
> I completely forgot systems of equations were a thing
> I should go back to high school
Well to be fair, I learned systems of equations in elementary school, when I was in fifth grade. So I should really be going back to elementary school.

I just straight up implemented an iterative method for part 1 (`main1.py`), knowing that I would probably see something outrageous for part 2 but persisting anyway. I actually got it first try.

While brainstorming how to optimize part 2 (while letting my brute force solution run in the background), I finally realized that I was looking at a system of equations. So I dusted off Sympy, but since I hadn't used it in a while I ran into trouble when trying to check whether numbers were integers (I used `.is_Integer` instead of `.is_integer`).

Quite a boring problem, although it showed me that I'm missing elementary school knowledge as a uni student, so I guess that's exciting in the sarcastic sense. Quite fitting for a [HOS entry](../README.md#hall-of-shame), although two in a row doesn't bode well for me.
