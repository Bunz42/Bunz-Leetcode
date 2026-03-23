# 55 - Valid Binary Search Tree

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/valid-binary-search-tree/question

## 1. Problem Description
```text
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
```

**Example 1:**

<img width="248" height="164" alt="image" src="https://github.com/user-attachments/assets/2b5d0110-76e0-4325-a2bb-6ab2eeefc59e" />

```text
Input: root = [2,1,3]

Output: true
```

**Example 2:**

<img width="247" height="162" alt="image" src="https://github.com/user-attachments/assets/4333e4f9-a019-4936-9e53-590d59b1b3d7" />

```text
Input: root = [1,2,3]

Output: false

Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.
```

**Constraints:**
```text
1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
```

## 2. My Approach
```text
How to think of the intuition:
- One of the constraints of a BST is that both the left and right subtrees are
also binary trees, so you know the recursive step is going to be calling the
isValidBST function on the two subtrees.
- Now we need to think of a condition to check to validate each subtree. 
- Notice that both the left and right subtrees of any parent tree must satisfy this condition to make 
the parent tree a valid BST, so we need to actually keep track of a max value for the 
left subtree and a min value for the right subtree and make sure values in those subtrees 
adhere to those conditions.
- So, we need to define our own dfs

High-Level Solution:
- Dfs through the tree with a max and min value for the left and right sides respectively in mind
- Base case: if the node we're running the dfs on doesn't exist it means we got
to the end without finding invalid subtrees so we can return true
- Check to see if the current node doesn't fall within the min, max boundary
- Run the dfs on the two subtrees of the current parent tree.
- For the left subtree, the max value changes to the node we just left
- For the right subtree, the min value changes to the node we just left
- We should AND the recursive dfs calls together because we need all of them to be
True in order to have a valid BST

Implementation:
- def dfs(node, min_val, max_val)
- if not node: return True (base case)
- if not (min_val < node.val < max_val): return False
- return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
- Outside dfs fcn: return dfs(root, float('-inf'), float('inf))
```

