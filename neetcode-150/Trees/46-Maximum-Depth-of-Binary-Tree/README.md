# 46 - Maximum Depth of Binary Tree

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/depth-of-binary-tree/question

## 1. Problem Description
```text
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path
from the root node down to the farthest leaf node.
```

**Example 1:**

<img width="283" height="454" alt="image" src="https://github.com/user-attachments/assets/551d076d-314c-4574-976f-e70167a6f600" />

```text
Input: root = [1,2,3,null,null,4]

Output: 3
```

**Example 2:**
```text
Input: root = []

Output: 0
```

**Constraints:**
```text
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
```

## 2. My Approach
```text
This problem is obviously a simplified dfs problem. Dfs is perfect for finding routes along which
you can traverse down the binary tree, so it's only natural that I dfs through the tree
and calculate its maximum depth.

But how do I do that? Well, let's consider this:
I can start from the root, then recursively calculate the max depth of its two child nodes,
because the maximum depth of a tree is just the max depth of its subtrees + 1 to account
for its own root node.

So, I just have to return 1 + max(leftDepth, rightDepth), because I want the biggest depth
of the two subtrees on each recursive call. Then, the algorithm works its way down the tree
recursively, treating each subtree as another binary tree with a root and other child nodes. 

What's the base case though? The base case occurs when the root node you're looking at has
no more child nodes, so it occurs once you get to a point where the root node is None, in
which case you return 0.
```

