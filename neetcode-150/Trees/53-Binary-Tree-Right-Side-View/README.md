# 53 - Binary Tree Right Side View

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/binary-tree-right-side-view/question

## 1. Problem Description
```text
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree,
ordered from top to bottom.
```

**Example 1:**

<img width="690" height="381" alt="image" src="https://github.com/user-attachments/assets/01e538c0-61cf-4d1f-bc02-5ad1048f5d3e" />

```text
Input: root = [1,2,3,null,4,null,5]

Output: [1,3,5]
```

**Example 2:**

<img width="920" height="501" alt="image" src="https://github.com/user-attachments/assets/5ae48d07-34e0-4437-b20e-13e08882315e" />

```text
Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]
```

**Example 3:**
```text
Input: root = [1,null,2]

Output: [1,2]
```

**Example 4:**
```text
Input: root = []

Output: []
```

**Constraints:**
```text
0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
```

## 2. My Approach
```text
How to think of the intuition:
- Try to think about what it actually means to be "visible from the right side"
- If you think about it, the last node counting from left to right on a given level
in the tree is the one "visible from the right" because it "blocks vision" of all the
nodes to its left.
- For example, if I had 5 nodes on a given level in the tree, and I counted 1, 2, 3, 4
5 from the left, the last node (5th) would be the one blocking nodes 1-4, so it'd be
the only one visible from the right side.
- The problem wants you to find every node that is only visible from the right, so you
just look at every level and find the rightmost/last node.
- Now that you know the problem has to do with a level-traversal, you can immediately
think of using BFS, since it's ideal for level-traversal in a tree.

High-Level Solution:
1. We want to traverse through the tree level by level, performing a Breadth-First-Search (BFS)
2. At each level of the tree, we find the rightmost node and add it to our array

Implementation:
1. Check to handle edge case where tree is empty
2. Define result array and initialize a queue for the bfs to track each level's nodes (initialize
it with just the root node in it for the very top level)
3. While loop to loop until the queue is empty (since once the queue is completely
empty it means you've traversed through all the levels because that means there were
no left and right nodes to append from the previous iteration)
4. Calculate the length of the current level (the length of the queue)
5. Pop every node in the level from the front of the queue with a loop (if the node you just popped
was the last node in the level [level_length - 1], then you add it to the result array)
6. Add the left and right children of each node you pop to the queue to represent the next level
7. After exiting the while loop, return the resulting array
```

