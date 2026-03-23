# 56 - Kth Smallest Integer in BST

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/kth-smallest-integer-in-bst/question

## 1. Problem Description
```text
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
```

**Example 1:**

<img width="248" height="164" alt="image" src="https://github.com/user-attachments/assets/ff111d5f-6c9a-4fa0-9b95-c2bb963627e4" />

```text
Input: root = [2,1,3], k = 1

Output: 1
```

**Example 2:**

<img width="330" height="266" alt="image" src="https://github.com/user-attachments/assets/c993ee82-31fc-494c-aace-58d29a61bd37" />

```text
Input: root = [4,3,5,2,null], k = 4

Output: 5
```

**Constraints:**
```text
1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000
```

## 2. My Approach
```text
How to think of the intuition:
- A no brainer solution is just to store all the nodes you visit in an array then sort it and return the k-th value
from the sorted array, but that's obviously too slow with an O(nlogn) time complexity.
- What else are we given in the problem description. Well, we know we're working with a BST so let's try to use that.
- Since this is a BST, we know that the nodes in the left subtrees are smaller than the root, and we know the right
subtrees are greater than the root.
- How can we use this information? Well, you can kind of think of a BST in a similar way to a sorted array. You go through
the array starting with the smaller elements then make your way to the bigger elements.
- For this problem, we want to find the kth smallest value, so if we just count 1, 2, 3, 4... every time we visit a "sorted"
node, once we get to k, we just return that value.
- So, we do an in-order DFS traversal to visit the nodes in the left subtree, then the root, then the right subtree. That way,
we're guaranteed to be visiting nodes in the correct order.

High-Level Solution:
- Base case: the node we're running the dfs on doesn't exist, just return back up
- Stopping Condition: we reach k on our counter
- Visit the left subtrees first and add to the count every time we backtrack up a node and process it.
- Visit the right side after the root and add to the count when we visit a node.

Implementation:
- variable to track count
- result variable
- def fcn for inorder traversal (node):
	- base case (also check if we already found a result so we can just return all the way back up)
	- recursive call on node.left
	- count increment
	- check count to see if it equals k. If so, update res variable and return
	- recursive call on node.right
- kick off the traversal on the root
- return result
```

