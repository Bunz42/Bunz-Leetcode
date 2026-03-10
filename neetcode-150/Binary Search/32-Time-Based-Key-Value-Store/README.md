# 30 - Find Minimum in Rotated Sorted Array

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question

## 1. Problem Description
```text
You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning.
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
```

**Example 1:**
```text
Input: nums = [3,4,5,6,1,2]

Output: 1
```

**Example 2:**
```text
Input: nums = [4,5,0,1,2,3]

Output: 0
```

**Example 3:**
```text
Input: nums = [4,5,6,7]

Output: 4
```

**Constraints:**
```text
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
```

## 2. My Approach
```text
Brute forcing this problem is super easy you just go through the array
and find the minimum element. However, this problem says you should
think of a better time complexity algorithm than O(n).

The problem says I should be aiming for an algorithm that runs in O(logn)
time, which immediately hints to me that I should use binary search.

But how can I use binary search? The array given isn't sorted, because it's
a rotated sorted array, and I can't just sort the array because that would
bottleneck the time complexity to O(nlogn), which is even slower than the
regular linear search.

So, how can I implement binary search in this case? Well, let's start by
defining how the whole rotation mechanic even works. The array being "rotated"
a specified number of times just means its elements have been shifted to the
right that many times, with overflowing elements cycling back to the beginning
of the array.

So, since the elements at the end of the sorted array are going to move
to the front 1 by 1, you're pretty much guaranteed that if there's a break
where the array isn't sorted anymore, you're going to end up with two distinct
sorted parts of the array.

For example, if you have the original sorted array [1, 2, 3, 4, 5] and you rotate
it twice, you'll get [4, 5, 1, 2, 3] which gives you the sorted partitions
[4, 5] and [1, 2, 3].

I can run binary search on the array with two pointers, each in two different
sorted segments. Then, I just find the middle between them, and two of the
three between l, r, and mid are guaranteed to be in the same sorted segment. 
Now, I just need to think of the condition I care about to eliminate one half 
of the search and observe the other half.

Let's think about this:
- If the middle pointer value is greater than the right pointer value, then that means
middle pointer is in the left sorted segment. Since the left segment is going to have
the bigger values in this case, the minimum value has to be to the right somewhere.

- Otherwise, that just means we're in the correct segment where the minimum is located, so
the minimum element has to be somewhere to the left or just straight up the mid element.

So, I just move the l and r pointers accordingly, but unlike the normal binary search,
we don't have a specified target value, so we actually can't move r to mid - 1, because 
we need to include the mid element just in case it is the minimum.

We just repeat this process and then eventually, our l and r pointers are going to land
on the same element, and that will be our minimum. Binary search brings our algorithm
from O(n) to O(logn).
```

