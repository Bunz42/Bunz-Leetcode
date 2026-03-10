# 31 - Search in Rotated Sorted Array

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/find-target-in-rotated-sorted-array/question

## 1. Problem Description
```text
You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
```

**Example 1:**
```text
Input: nums = [3,4,5,6,1,2], target = 1

Output: 4
```

**Example 2:**
```text
Input: nums = [3,5,6,0,1,2], target = 4

Output: -1
```

**Constraints:**
```text
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
All values of nums are unique.
nums is an ascending array that is possibly rotated.
```

## 2. My Approach
```text
This problem is quite similar to the one I did yesterday, which was called
Find Minimum in Rotated Sorted Array.

The trick to that problem was realizing you can split a rotated sorted array
into two sorted segments, then you can run binary search on the segments
and throw away certain halves of the search based on which sorted segment
your mid variable is located in.

This problem is really similar. The only difference now, is that instead of
finding the minimum element, you're searching for a target element.

Let's start by looking at it through the same lens we did for the last problem.
Break the array into two sorted segments, the left and right. Then, define two
pointers, each in distinct segments, and begin the binary search by finding
the middle index.

If the middle value is already equal to the target, then great we can just
return the index it's at because we found the target.

However, if this isn't the case, we need to perform some more checks to find
the target. Let's start by asking ourselves:
"What happens if the target is in the left sorted segment?"
How can we perform checks to verify that, and what can we do with that info?

Well, you know you're looking at the left segment if the value at your left
pointer is lower than the one at your mid index, because imagine if the
mid index was less than your left pointer. Since you rotated the array, the
bigger values are going to overflow to the start of the array, so if you're
mid index was less than your left pointer, it means you'd be looking at the
smaller values in the right sorted segment.

Now, if you're looking at the left sorted segment, how can we check if the
target value is actually in this segment? We just compare to see if its in
between the left pointer value and the middle value. If it is, it has to be
in this segment so we drop the right. If not, it's going to be in the right 
segment, so we drop the left.

Similar logic applies to the right segment. If nums[l] is not less than or equal
to nums[mid], then we know we're looking at the right sorted segment instead.
So, now we just check if the target is between the middle and right values. If it
is, then the target is in the right segment and we can drop the left. If not,
the target is in the left segment and we drop the right.

We repeat this until the left and right pointers eventually land on top of the
target, or become invalid (which therefore indicates the target isn't even there).
We return -1 if the target was never found.
```

