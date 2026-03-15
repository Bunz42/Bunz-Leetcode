# 47 - Diameter of Binary Tree

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/binary-tree-diameter/question

## 1. Problem Description
```text
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree.
The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.
Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.
```

**Example 1:**

![Example 1](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/90e1d7a0-4322-4c5d-c59b-dde2bf92bb00/public)

```text
Input: root = [1,null,2,3,4,5]

Output: 3

Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].
```

**Example 2:**
```text
Input: root = [1,2,3]

Output: 2
```

**Constraints:**
```text
1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
```

## 2. My Approach
```text
I'm going to start by thinking about what the diameter of a binary tree actually is.
The problem tells me it's the longest distance between any two nodes in the tree,
not necessarily passing through the root.

So, how can I find the longest diameter if I were to just think about it logically.
Well, I need to think about under what scenario I would get the largest distance
between two nodes given a particular subtree. The longest distance is just going to
be the distance between the deepest node on the left side of the subtree, and the
deepest node on the right side of the subtree. This is guaranteed to work for any
subtree because if there's a defined left and right depth, you always have a path
between their nodes because you have the root of that subtree to pass through.

Now that I know how to find the max diameter of a given subtree, how do I find the
diameter of the bigger tree? Well, I just have to dfs through the tree and evaluate
the diameters of all the possible subtrees, tracking the max diameter I found overall
throughout the entire process.

How do I implement this?
1. Make variable to track biggest diameter seen so far
2. Define a dfs helper function
3. Base case: if not node: return 0
4. Run dfs on the left and right children/subtrees to find
their depths.
5. Update the diameter variable to the max between itself
and the total distance between the deepest left node and
deepest right node max(self.diameter, leftDepth + rightDepth)
6. Return 1 + max(leftDepth, rightDepth) to return the height
of the subtree.
7. Call the function on the root and return the resulting diameter at the end.

```

