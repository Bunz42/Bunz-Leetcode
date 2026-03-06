# 28 - Search a 2D Matrix

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/search-2d-matrix/question

## 1. Problem Description
```text
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
```

**Example 1:**

<img width="406" height="301" alt="image" src="https://github.com/user-attachments/assets/f3ff5a60-a86f-4bb6-9ff8-7ea6d3e38675" />

```text
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
```

**Example 2:**

<img width="407" height="302" alt="image" src="https://github.com/user-attachments/assets/1d97fbe1-ed1d-4bf6-b295-cb3e687d1185" />

```text
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
```

**Constraints:**
```text
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
```

## 2. My Approach
```text
To brute force this problem, you can just do a linear search through the
2D matrix to find the target element. However, this would require a nested
loop, which would make the time complexity O(m*n), which is quite slow.

Since the problem specifies that you should aim for a solution with a time
complexity of O(log(m*n)), and that the array is sorted in ascending order
along its rows, this is a pretty dead giveaway that you can
instead implement some form of the binary search algorithm to find the 
target element instead.

However, binary searching through a 2D matrix is not as trivial as searching
through a linear data structure like an array, so how can I come up with
a version of its implementation that allows me to search through this matrix?

Well, let's think back to the most fundamental implementation of binary search:
you evaluate the middle element, then based on that element's value, you shift
the interval you're checking based on the logic that the target value must be
within that interval. You then repeat this process, shrinking the interval
you're checking until, in the worst case, you get an interval of size 1 where
the element is either guaranteed to be the target value, or guaranteed to not
exist in the data structure.

So, how can we kind of adapt this for a 2D matrix? Well, we can think of the
rows of the 2D matrix as intervals. Since the elements in each row are
guaranteed to be greater than the elements of the preceding row (as specified
in the problem) I can use the intervals created by these rows to make logical
decisions pertaining to the location of the target value.

How exactly would I go about doing this? Well, first I need to identify which
row the element is actually going to fall into, and I can do that by running a
binary search on the rows. This operation will take O(logm) time where m is
the number of rows.

Then, I need to actually find the element within the row, and at this point the 
problem is just as trivial as the fundamental binary search, because a single row
within a 2D matrix is just a linear array of data, so we can just run the normal
binary search on the specified row. This will take O(logn) time where n is the
number of columns/number of values in each row.

How do I implement the binary search row identification? I can start by realizing
that I only care about the biggest and smallest elements of each row, which occur
in the last and 1st columns respectively (as specified in the problem). With this in 
mind, I know that if the target value is greater than the biggest value in a row, it
has to be in one of the rows after. If it's smaller than the smallest value in a row,
it has to be in one of the rows before. Otherwise, it's just in the row you're
looking at currently.

Implementation in python:
1. Initialize variables storing the number of rows and columns using len(matrix) and 
len(matrix[0]) respectively.
2. Initialize top/bottom row variables to 0 and rows - 1
3. While top <= bot, find the middle row with (top + bot)//2
4. Check if the target is less than the smallest value in the mid row (matrix[row][0]).
If it is, shift the bottom row to the mid row - 1
5. If not, check if the target is greater than the biggest value in the mid row (matrix[row][-1]).
If it is, shift the top row to mid row + 1.
6. If none of these are met, then the target is within the current row, so you can just break out
of the loop.
7. Once we exit the loop, check to see if top <= bot, if not then the target isn't in any of the
rows, so we just return False immediately.
8. Find the row the element is in again using (top + bot) // 2
9. Initialize the left and right columns as 0 and columns - 1
10. Run binary search on the row (see solution for more details)
```

