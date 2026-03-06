# 27 - Binary Search

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/binary-search/question

## 1. Problem Description
```text
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.
```

**Example 1:**
```text
Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
```

**Example 2:**
```text
Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
```

**Constraints:**
```text
1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.
```

## 2. My Approach
```text
This problem is literally just the basic implementation of the classic
binary search algorithm.

Normally, searching through an array by just iterating through every element
would have a time complexity of O(n), since each element in the array is checked
once. However, with binary search, you can avoid checking some of the elements by
breaking up the array into relevant halves on each iteration.

Here's the idea:

I'll start by checking the element in the middle of the array. This middle
index can be calculated with the formula (low + high)/2, with low being the
leftmost index in the array and high being the rightmost index.

If the middle element is just the target I'm searching for, then cool, I
can just return it.

If it's not, what condition can I use to efficiently reduce the number of 
elements I need to check? Well, I know the array is sorted in ascending order,
so let's say the element I just checked is greater than the target, well that
means I know the target has to be in the left half of the array, and in the right
half if the middle element was instead less than the target.

So, I can just completely ignore one half of the array if it's not relevant, meaning
all I need to do is "shrink" the area I'm looking at into the desired subarray by
moving my high or low accordingly.

Then, I just repeat the process until I either find the element I'm looking for, or 
in the worst case scenario I get to a point where I shrink the area I'm observing
into a subarray of length one, which at that point will be guaranteed to be the target
I'm searching for, or will indicate to me that the target isn't present in the array.

This searching algorithm has a time complexity of O(logn) because you're taking
at most logn partitions of the array.

Here's how I'll implement it in python:
- Initialize two variables l and r to track the low and high indices that will bind the
subarray I'm observing. Start l at the 1st index and r at the last index.
- Then, while low <= high, I'll find the midpoint, compare it to the target.
- Midpoint will be calculated with (l + r) // 2
- If midpoint < target, I'll move l to midpoint + 1
- If midpoint > target, I'll move r to midpoint - 1
- Keep doing this until you find the target or you get to the point where low > high (which
means the leftmost and rightmost indices are going to be right on top of each other,
making the subarray size 1)
- If the target isn't found before this condition is met, then that just means it was never
in the sorted array to begin with, so I'll just return -1 outside the loop.
```

