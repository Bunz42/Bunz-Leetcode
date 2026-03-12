# 33 - Median of Two Sorted Arrays

**Difficulty:** Hard | **Link:** https://neetcode.io/problems/median-of-two-sorted-arrays/question

## 1. Problem Description
```text
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order.
Return the median value among all elements of the two arrays.

Your solution must run in O(log(m+n)) time.
```

**Example 1:**
```text
Input: nums1 = [1,2], nums2 = [3]

Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.
```

**Example 2:**
```text
Input: nums1 = [1,3], nums2 = [2,4]

Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.
```

**Constraints:**
```text
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
-10^6 <= nums1[i], nums2[i] <= 10^6
```

## 2. My Approach
```text
This problem looks pretty easy at first, because you'd think you can just
merge the two sorted arrays into a bigger sorted array using two pointers
or something. Then, you just take the middle value if the array has an odd
size, or the average of the two middle values if the array has an even size.
However, this problem is a hard, so they're obviously not going to let you get 
away with it that easily.

The problem specifies that you need a time complexity of O(log(m + n)), which
makes this problem a lot harder than just merging the two arrays into one. The
previously mentioned merging solution is O(m + n), so you can't really do that.

Both of the arrays are sorted in ascending order, and the problem is asking me 
to search for an element (the median) using an algorithm that runs in logarithmic
time. This instantly indicates that I can potentially use binary search for this
question.

Let's start by thinking about what the median of the two sorted arrays would even
look like. Let's pretend I did actually merge the arrays together, then there
would be (m + n)/2 elements before the median, where m and n are the lengths of the
two sorted arrays. 

So, basically when you're finding the median of a set of numbers, you're just cutting
it so that half of the total number of elements are to the left of the cut, and half
are to the right. You also need to make sure the numbers to the left are less than the
numbers to the right and sorted in ascending order.

What I'm getting from this is that I somehow have to take two arrays and manipulate
them in some way so I can kind of treat them like a single merged array with a "cut"
that helps me find the median of the elements. I need to search for a valid partition
that slices through both arrays at the same time and ensures half the total values
between the two arrays are to the left of the cut, and half the total values are to
the right. Since the arrays are sorted in ascending order, I can use this to my advantage
to find a valid partition that satisfies the conditions for finding a median.

How in the world am I going to do this? Let's start by thinking about a case where I have
two sorted arrays, each of size 5. If I were to think about merging them together, I'd get
a sorted array of size 10, so if I were to cut it down the middle, the perfect left half
would have 5 elements in it.

Let's say I cut the first array at its 3rd element, meaning I take 3 elements from array A.
Well, how many elements would I be able to take from B to fill that 5 element left half? I
would need to take 2. This applies in any case, where cutting through array A at index i
results in a cut being made in array B at index half_length - i. 

How does this information help me in any way? Well, it tells me that I can restrict my 
search space for the partition to only the smaller of the two arrays. Why is that? 
Well, think about if I binary searched for a partition in the bigger array first. Imagine
I had an array of size 2 then a bigger one of size 10. The half length in that case is 6,
but let's say I searched through the size 10 array and made a cut at index 8, well then
I'd need to take 6 - 8 = -2 elements from the smaller array to hit that half length of 6,
which just doesn't make any sense for obvious reasons.

So, restricting the search space to the smaller array guarantees that I'm going to end up
with a positive, valid number of elements to take from the bigger array. It also bumps my
time complexity down from log(m + n) to log(min(m,n)), which is even quicker.

Okay, now that I got that part out of the way, I need to address the most difficult part:
how do I actually implement this partition search? Well, let's call the smaller array A
and the bigger one B, then imagine what would happen if I made a cut in the middle of A.

When I make a cut in A, there will be a corresponding cut made in B calculated using the
half_length - i logic. When I make these two cuts, I only really care about the 4 elements
surrounding the cuts. These 4 elements are the two on either side of the cut in A, and the
two on either side of the cut in B. How do I know if the cuts I just made are actually a
valid partition?

Well, if you think about it, we already know that the value to the left of A's cut is less
than the one to its right, since the array is sorted. The same goes for array B's cut. So,
we only care about the cross section between them. How would you merge the two cuts together
to see if you actually have a valid sorted array after?

Let's think about it like this. When I'm making a cut in the array, I'm basically saying that
if I took all the elements from the left side of the partitions in each array and dumped them
in a bucket, then I did the same to the elements from the right side of the partitions, the
left bucket's elements will be less than or equal to the ones in the right bucket. This means
the left side values must be less than both the right side values. Since we already know that
the left of A and B's cuts are less than/equal to their respective right side counterpart, we 
only really need to check that the left of A is less than or equal to the right of B, and that
the left of B is less than or equal to the right of A. If this is the case, we found a valid
partition.

What happens if our partition is invalid? Let's say A's left side value is too big, then that
means we have too many big values from A, so we want to move A's cut to the left, so we drop 
the right half. What if B's left value is too big? Then, A's cut is too small, so we need bigger
numbers. So, we move A's cut to the right by dropping the left half.

If we repeat this process, we'll eventually find a valid partition, then we can finally find the
median. If the total number of values is odd, the median will just be the smaller number on the 
right side of the cut between A_right and B_right. However, if the total number of values is even,
then the median will be the average between the maximum value on the left and the minimum value on
the right of the cut.
```

