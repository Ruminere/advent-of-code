# Problem 12
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 4320 | 4902 |
| Time | 00:37:26 | 02:22:11 |

**Addendum, more than 16 hours after the problem dropped**: Although most of this rant is about part 2, I just realized that I did not need to make part 1 so complicated. I kept track of all the letters, which meant that I also kept track of the number of times I'd seen each letter to account for letters showing up more than once. I did not need to keep track of the letters themselves. Dang, would've saved me so much time on part 1.

Today I learned that sorting by index 1 in Python doesn't mean that it will be sorted by index 0 automatically.

This took way longer than it needed to. I first tried to find whether a edge coordinate's neighbors were already in some set of edges, but that would not work for the following case, where 1 is the plot, since `0` is a corner and is involved in more than one edge:
```
10
11
```
I tried very hard to catch edge cases, but to no avail; I kept on either undercounting or overcounting.

Then I decided to categorize everything by direction. I had two cases: up and down. Nothing worked, until I printed everything out and saw that my array was unsorted, so I sorted it without thinking much. My solution made both cases undercount by 1, but I added `4` to `edges` at the end of my function so that this wouldn't be an issue.

Now, keep in mind that the coordinates are ordered as `(row,col)`, so now for left/right cases I had to sort by index 1. I did this by using `sorted(edges_raw[d], key=lambda i:i[1])`. I went absolutely crazy after seeing my modified up/down not work and tried seeing the comparisons being made between each coordinate (this was actually how I found the undercounting by 1 bug), until I printed this out (derived from the bigger sample input):
```
(0, -1) [(4, -1), (2, -1), (3, -1), (5, -1), (6, -1), (5, 2)]
3
(0, 1) [(2, 2), (3, 2), (6, 2), (5, 2), (4, 4), (5, 4)]
2
V0 13 12
```
Looking at the array for `(0,-1)` (left case) made me so angry. I thought that Python would automatically sort by index 0 when I sorted by index 1, the same way that Python would automatically sort by index 1 when I used `sorted()` without a key. I thus used normal sort first, then sorted by index 1 to fix the issue.

I was just so done when I saw the `1206` pop up on my screen, so I tiredly Ctrl-Z'ed to my actual input and finally got the correct answer.

I think I'm too sleepy to be angry. I need sleep. But I need to finish grading people's homework since I'm a TA for an intro Python class...

But hey, about time for another [hall of shame](../README.md#hall-of-shame) entry! Really feeling the "shame" part tonight.
