# 26 - Largest Rectangle in Histogram

**Difficulty:** Hard | **Link:** https://neetcode.io/problems/largest-rectangle-in-histogram/question

## 1. Problem Description
```text
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.
```

**Example 1:**
```text
Input: heights = [7,1,7,2,2,4]

Output: 8
```

**Example 2:**
```text
Input: heights = [1,3,7]

Output: 7
```

**Constraints:**
```text
1 <= heights.length <= 1000.
0 <= heights[i] <= 1000
```

## 2. My Approach
```text
This problem is asking you to find the largest possible rectangular area
that you can form with the bars in a histogram, which is a chart where
all of its bars are touching the preceding and following bars.

To determine the area of a rectangle formed by the histogram, you can take
the shortest bar within a grouping of bars, then extend it left and right
until you hit an even shorter bar, then calculate the area using the width
of the interval multiplied by the height of that extended bar. This works 
because if you visualize how rectangular areas are formed in a histogram, 
you will realize that they are bottlenecked by the shortest bar within a
given interval.

So basically, the problem is asking "if I force this bar to be the shortest
part of my rectangle, how far can I stretch it to the left and right before
it gets blocked by a shorter bar?"

A brute force approach to this problem would be to iterate
through every single bar, extending it left and right to find the area it
creates, then updating a maximum area variable accordingly. However, this 
approach is super slow with an O(n^2) time complexity.

However, there's a better way to solve this problem by pre-calculating
the boundaries that a bar can extend to, then finding the height from there.
To do this, we need some way to find the 1st occurrence of a shorter bar
to the left of the current bar, then the 1st occurrence of a shorter bar
to the right of the current bar.

How can we find the boundaries? We can use a stack where we store indices instead of
heights. Specifically, we need to use a monotonically increasing stack, and I'll
explain why in a bit. Think of it like this: as we iterate through the histogram,
we first care about finding the right boundary of a given bar, and since that only
happens when we find the 1st shorter bar to the right of the current bar, we can just
keep pushing the positions of taller/equal bars onto the stack, until we find the
shorter one. 

Now, remember, as we store the positions of pillars, we want to immediately calculate
a valid area whenever there is one. So, as soon as we find a shorter pillar, instead
of pushing it into the stack, we pop the taller bar from the top of the stack
and calculate its area using the height at that corresponding position, then we keep 
doing that for all the bars in the stack until the short bar we just found isn't the
shortest anymore. In that case, we can finally push the short bar onto the stack and
keep going through the array.

Okay, so we found the right boundary for each of the bars in the stack, but what
about the left boundary? Well, the beauty of this problem is that since you're
storing the bars in monotonically increasing order, it means that whenever
you calculate an area for a bar, the bar to the left of it (right below it
in the stack) is guaranteed to be shorter than the current bar, meaning it's always
going to be the left boundary. So, with that in mind, you can calculate the area.

Now, we have the appropriate algorithm to calculate the maximum areas that can be
formed by each bar by storing their positions in the histogram in an increasing 
order of height, so we just have to update a max variable every time we calculate
a height, and then we'll get the right answer. This solution is O(n) because even
though there's going to be a while loop in the solution, every element in the array
is only pushed and popped once.

Note: in the case that the stack is empty, the interval width is just equal to the
index of the right boundary. Otherwise, it's going to be i - top of stack - 1 after
popping the desired bar to make the left boundary the new top of the stack.

Note: I also need to account for the fact that if there are going to be some bars
whose right boundary is just the end of the array, because they might just not have
a shorter bar to their right. So, I just need to include a final loop at the end
to flush out the areas of the remaining bars that weren't included in the stack
algorithm.

```

