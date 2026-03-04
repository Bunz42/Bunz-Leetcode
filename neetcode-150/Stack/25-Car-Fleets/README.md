# 24 - Daily Temperatures

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/daily-temperatures/question

## 1. Problem Description
```text
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before
a warmer temperature appears on a future day. If there is no day in the future where a
warmer temperature will appear for the ith day, set result[i] to 0 instead.
```

**Example 1:**
```text
Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
```

**Example 2:**
```text
Input: temperatures = [22,21,20]

Output: [0,0,0]
```

**Constraints:**
```text
1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100
```

## 2. My Approach
```text
You could brute force this problem by just iterating through the array of temperatures
then checking every subsequent temperature to find the first occurrence of a warmer
temperature, storing the number of checks performed at the ith index of your result.

However, this would be an O(n^2) solution, which is very slow. You're intuition will
probably try to tell you that this problem must be solved by checking elements in a
standard front to back order, but what if we change the way we think about this problem?
What if, instead of just checking elements in a standard manner, we apply the logic in
the reverse direction?

For example, what if we start at an element somewhere in the array that isn't the start,
then compute all the results for each of the temperatures before it? There's a data structure
that can help us with this, and it's a stack. Specifically, a monotonic stack, which is a
stack that maintains a strictly increasing or decreasing order by popping elements before
pushing new ones.

For this problem, we need to use a monotonically decreasing stack where we pop indices where
the values are smaller than the current temperature we're checking. This is useful because you
can push temperatures that are already in decreasing order into the stack naturally, since the
problem only cares about the first time a temperature is greater than a previous temperature.
Then, when you encounter a temperature that's greater than the temperature at the top of the stack,
you can just pop elements from the stack, calculating the number of days after the ith day the
greater temperature appears with the difference between the two indices and storing the difference. 

Then, once you pop and evaluate all the temperatures that are less than that pending temperature, you
can finally push it onto the stack, maintaining a strictly decreasing order. Then, you just repeat the
process, and you're guaranteed the right result.

However, keep in mind that the problem specifies that you need to store a value of 0 for temperatures
that don't happen to have any greater temperatures occurring after them. So, a way to get this done
is just to initialize the result array with all 0s, then just replace only the relevant indices with
a new value, because only the temperatures that actually have greater temps occurring after them will
be evaluated with this stack algorithm.

Also, another complexity in this problem that I just realized is that when you pop elements from the
stack to maintain its monotonic order, you're going to lose the indices of your temperatures, which
you need to create the proper result array. So, you can't really only store the temperature values.
You need to push temperature-index pairs instead, so that you can always access the correct index
of a given temperature.

With all these parts of the solution in mind, here's the implementation for the new O(n) solution:
- Initialize the stack
- Initialize the result array with all 0s
- Iterate through the temperatures
- While the current temperature is greater than the temperature on the top of the stack, pop
temperatures, calculate the index difference, then store it in your result array.
- When the current temperature isn't greater than the top of the stack, just push it in as a
value-index pair
- Return the result array
```

