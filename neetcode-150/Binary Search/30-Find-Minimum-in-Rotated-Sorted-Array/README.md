# 29 - Koko Eating Bananas

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/eating-bananas/question

## 1. Problem Description
```text
You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k.
Each hour, you may choose a pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, you may finish eating the pile but you can
not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.
```

**Example 1:**
```text
Input: piles = [1,4,3,2], h = 9

Output: 2

Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1,
you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.
```

**Example 2:**
```text
Input: piles = [25,10,23,4], h = 4

Output: 25
```

**Constraints:**
```text
1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000
```

## 2. My Approach
```text
To start this problem, I need to understand that the time it takes
to get through a singular pile with x bananas if I'm eating at a rate
of k bananas an hour is just ceil(x/k). I need to round up because
I'm not allowed to start on the next pile in the same hour I just
finished a pile, which means the number of hours will be an integer.

I then need to realize that the problem explicitly tells me in the 
constraints that the number of hours h you get to eat all the bananas 
is guaranteed to be greater than or equal to the number of piles.

So, given that I can only eat k bananas in a given hour, I now know that
there is a k value which guarantees that I can finish the bananas
in time. This k value is just equal to the number of bananas in the
biggest pile, since if I can finish that pile in an hour, it's
pretty obvious that I can finish any other pile in an hour as well.
Since the number of hours I get is going to be at least the number
of piles, I know I can definitely finish all the piles at this rate.

This gives me the upper bound of my answer k, but there's also 
smaller values of k that will allow me to finish the piles in
the given time limit, because you can eat the piles in any order.
This is why the problem is asking to find the minimum k value that
still lets me finish all the bananas.

How do I do this?
Well, I could choose to brute force this problem by just iterating
through k values from 1 to whatever the upper bound is, then checking
whether or not each one is valid, and tracking the minimum valid
k value. 

How do I check if a specified k value can work though?
Well, you just go through each pile, find the time it takes to get
through that pile by using ceil(pile/k), then add that to a sum. Then,
you check if that total time is less than or equal to h to see if it's
valid or not.

However, this is going to be super slow, because I need to loop through
every one of the n piles for every k value, making the time complexity O(m * n),
with m being the number of k values (which is just equal to the upper bound)

How can I reduce the time complexity of this operation?
I realized that I'm pretty much just performing a linear search through a
set of possible k values and looking for the minimum one that works. However,
since the possible k values go from 1 to the upper bound in increasing order,
I can just treat it like an array of values sorted in ascending order.

What algorithm can I use to search through a sorted array faster than I can
with linear search? The answer is binary search. I can write a binary search
algorithm to find the perfect k value.

I'm going to adapt the classic binary search implementation by finding the
middle k value, iterating through all the piles to calculate the total time
it would take to eat all the bananas, then checking if its lower than h. If
it is, cool I found a possible k value, so I can record it by updating a minimum 
variable accordingly. Then, since we already found a possible k value, I know that we
can just cut off the entire right half of the array since I only care about
even slower rates that still allow me to finish all the bananas.

In the other case, where the time for that middle k value exceeds h, I know
now that it's invalid, and of course there's no possible way that any slower
k values can allow me to eat all the bananas in time if a faster rate doesn't,
so I can just cut off the left half of the array and try to find a k that works.

I can just keep running this and return the minimum value at the end.
```

