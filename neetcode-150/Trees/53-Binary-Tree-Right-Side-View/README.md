# 52 - Binary Tree Level Order Traversal

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/level-order-traversal-of-binary-tree/question

## 1. Problem Description
```text
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of
nodes at a particular level in the tree, from left to right.
```

**Example 1:**

<img width="349" height="255" alt="image" src="https://github.com/user-attachments/assets/903a9144-d298-40aa-8d79-15fa7020ad09" />

```text
Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
```

**Example 2:**
```text
Input: root = [1]

Output: [[1]]
```

**Example 3:**
```text
Input: root = []

Output: []
```

**Constraints:**
```text
0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
```

## 2. My Approach
```text
For this problem, instead of going down one route at a time all the way to the bottom then
backtracking up like in dfs, I'm asked to traverse the tree by level. I need to read the tree
layer by layer, so the proper algorithm for this is actually Breadth-First Search (BFS).

BFS relies on a queue data structure, and in the case of this problem, it seems appropriate to
store the nodes in the queue. Store the root first, then pop it and append it to an array for
its respective level, then do the same for both its children, and so on. Every time a node is
popped from the queue, I'll add both its children to the queue (so they'll "get in line" behind
the remaining nodes of that level and wait to be processed in the correct order). I'll repeat
this process, appending nodes appropriately until the queue is empty.

To implement this:
1. Check edge case where tree is just empty, return []
2. Initialize the result array and our queue with the root node in it
3. Keep running a while loop until the q is empty
4. Find the length of the current level
5. Initialize an array to store the current level's nodes
6. Process enough nodes to fill the length of the level by popping them
from the front of the queue (for loop).
7. Append the popped node to the level node array
8. If the node has a left child, append it to the back of the queue
9. If the node has a right child, append it to the back of the queue
10. After processing all the level's nodes, append the array to the result
11. Return the result at the end of the while loop.
```

