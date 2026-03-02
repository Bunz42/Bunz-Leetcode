# Bunz' Comprehensive Two Pointers Algorithm Guide
## What exactly is two pointers?  
Basically, two pointers is just exactly what it sounds like. Instead of iterating
through a data structure with just one reference, you use two references instead and
move them both simultaneously.

Two pointers works on linear data structures like arrays, strings, or linked lists, and
it replaces the typical "single loop going through elements one by one" approach with
two pointers navigating through the data structure starting from various positions and
moving at various speeds.

## What is it for?
The whole point of the two pointers algorithm is to optimize your time complexity. Usually,
two pointers helps you move from an O(n^2) nested loop solution to a cleaner, O(n) solution.

Another thing it does it reduce your space complexity, since you can use two pointers to solve
a lot of problems directly in place within the data structure, you rarely ever need to allocate
any extra memory. All you need to do is store two index variables!

## The Big Three
The way I like to think about two pointers is: there's a "big three" or three main types of two
pointers problems.

### 1. The Opposite Ends
This is where one of your pointer starts at the very beginning, and one starts at the end. Then,
you move the pointers inwards until they meet.

When do you use opposite ends?  
This approach is probably the most common, and a giveaway you should look for is when the problem asks
you to do something to a sorted linear data structure. Since the data is sorted, you're usually 
able to make some smart decisions about which pointers to move based off of whether your current 
result is too big or too small.

This approach is also commonly used to find pairs or triplets, like in Two Sum and 3 Sum, or Container With
Most Water (which is a "pair" of heights)

What are some classic examples?
- In the famous Two Sum problem on leetcode, where you need to find a pair of integers
in an array that sum up to a target value, you can sort the array, then define pointers at 
opposite ends, moving the left one inward if your sum is too small, then moving the right one
inward if its too big.
- In Valid Palindrome, you need to check characters in alternate corresponding positions (for example
the 1st element would correspond with the last element, the 2nd element would correspond with the 2nd last,
etc.) so you can define pointers on opposite ends then move them inward.
- In Container With Most Water, you define your pointers at opposite ends then move the pointer that
references the shorter line inwards to maximize area.

### 2. Same Direction/Fast and Slow
This is where both pointers start at the beginning but move at different speeds or with a fixed gap between them.

When do you use Same Direction?  
This one's pretty common for linked list problems, or for some in-place array modification problems

What are some classic examples?
- Finding the middle of a linked list: when your fast pointer reaches the end, your slow pointer will be in the middle
- Remove Duplicates from Sorted Array: one pointer scans, the other keeps track of where to place the next unique

### 3. Two Iterables
This one's a bit more niche, and it's essentially where you're given two data structures to iterate through, so you
go through them both at the same time using two pointers.

When do you use Two Iterables?
This one's mostly for comparing, merging, or finding intersections between two datasets.

What are some classic examples?
- The only one I can think of at the moment is merging two sorted lists in merge sort. You define one pointer in the
1st sorted list, then another in the 2nd sorted list, then you iterate through both of them and compare their values,
picking the smaller one every time to build the new merged list.

## Summary of How to Spot Two Pointers
If you're looking at a coding problem on an interview, look for these giveaways:
- Linear data structure
- Sorted linear data
- You need to find pairs or triplets
- You need to operate in-place
- Linked list
