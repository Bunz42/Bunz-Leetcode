# 45 - Invert Binary Tree

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/invert-a-binary-tree/question

## 1. Problem Description
```text
You are given the root of a binary tree. Invert the binary tree and return its root.
```

**Example 1:**

![Example 1](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/ac124ee6-207f-41f6-3aaa-dfb35815f200/public)

```text
Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]
```

**Example 2:**

![Example 2](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/e39e8d4f-9946-4f99-ee3d-0d4df08d4d00/public)

```text
Input: root = [3,2,1]

Output: [3,1,2]
```

**Example 3:**
```text
Input: root = []

Output: []
```

**Constraints:**
```text
0 <= The number of nodes in the tree <= 100
-100 <= Node.val <= 100
```

## 2. My Approach
```text
This problem is just simple tree depth first search (dfs). It's not really
typical dfs though because it's actually even simpler than normal dfs problems.

The way to solve this problem is just to swap the child nodes of the root using
root.left, root.right = root.right, root.left.

Then, you want to that for every subtree as well, so you just recursively call
the inversion function on the child nodes root.left and root.right as well,
returning the root of each inverted subtree until you finally backtrack to the
original root and get a fully inverted binary tree.

The base case for this problem is just when you get to a point in your tree where
your root doesn't have any more child nodes to invert, so it's just when the next
root you're checking doesn't exist (None).
```

