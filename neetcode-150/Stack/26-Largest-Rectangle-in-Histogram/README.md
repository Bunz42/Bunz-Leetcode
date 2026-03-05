# 25 - Car Fleets

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/car-fleet/question

## 1. Problem Description
```text
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it.
It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed.
A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination,
then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
```

**Example 1:**
```text
Input: target = 10, position = [1,4], speed = [3,2]

Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.
```

**Example 2:**
```text
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10.
The cars starting at 1 and 0 never catch up to the car ahead of them.
Thus, there are 3 car fleets that will arrive at the destination.
```

## 2. My Approach
```text
This problem is pretty tricky, because it's pretty hard to visualize the
cars, and it's kind of hard to come up with an algorithm that determines
whether or not two cars will form a fleet, because you need to consider both
where they start and their speeds. Just because a car is faster than another
car, doesn't mean they will necessarily form a fleet, because one car might
already be near the end, so the faster car won't catch up in time.

Let's start by going over what I know must be a condition for a car to form a 
fleet with another car. I know for a fact that the only way is if the car behind
another car is travelling at a faster speed. This indicates to me that we only
care about the times when a car is BEHIND another car.

With this fact in mind, I want to find a way to simplify the problem a bit so that
I have something to work with. I was thinking of sorting the positions in ascending order,
to make every car start behind another car, then doing something with their speeds, but
after thinking about it for a while, that doesn't really help with anything. This is
because if I sort the cars in ascending order, it's still kind of hard to clarify what
their final speeds at the target destination are going to be because the car you once
thought would only form a fleet with the previous car might form a fleet with another car
ahead of it, and everything just gets very messy.

So, instead, now I'm thinking that maybe it's better to sort them in descending order, because
this will actually tell me good information about the final speeds of each of the cars, since
the car at the front is guaranteed to be travelling at its original speed, and then from there
it seems like you can kind of manipulate the other car speeds around that fact.

In order to actually find whether or not a car will form a fleet with the car ahead of it, I need
to know the amount of time it would take for each car to reach the final target, regardless of its
position. If I can find the time it would take for each car to get to the destination, I know that
cars that take less time to reach the end than cars in front of them are guaranteed to form a fleet.
To calculate the amount of time a car is going to take to reach the destination, I can just take the
difference between the target and current position, then divide it by the speed.

But, now I need to actually keep track of the time taken by the fleets I find, because fleets might form 
fleets with other cars in front of them, but cant form other fleets with cars behind them. A helpful
data structure for maintaining this sort of "ordering" where elements can't get in front of other elements
before they leave would be a stack. So, I can use a stack to track the times of each fleet.

I can iterate through the array (which will be sorted in descending order) and calculate the time each
car will take to reach the target, then if a car ever takes a lower or equal amount of time than the fleet
at the top of the stack it just joins the fleet. Otherwise, it'll form a new fleet (because the problem says that
a single car is also considered a fleet), and I can push its time onto the stack as a new fleet.

At the end, the size of the fleet stack is just going to be the number of fleets, so I can just return it.
Problem solved!

Note: there's a problem because when I sort the position array in descending order, I also need to change the
speed array so that they align properly. I actually didn't know this, but there's a function in Python ".zip()"
that locks the two arrays into alignment with each other by storing them in a list of tuples. Then, when you call
the sort function on the array, it'll only sort by the first element in the tuples, so it'll only sort by position,
but the tuples will still exist and have the correct associated speeds

Note: this solution has a time complexity of O(nlogn). The actual algorithm is O(n) but the problem is sorting
bottlenecks the time complexity to O(nlogn) unfortunately.

```

