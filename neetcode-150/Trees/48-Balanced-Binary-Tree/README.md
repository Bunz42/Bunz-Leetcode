# 48 - Balanced Binary Tree

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/balanced-binary-tree/question

## 1. Problem Description
```text
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right
subtrees of every node differ in height by no more than 1.
```

**Example 1:**

![Example 1](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/c19c3727-ea28-416c-3873-79ee75f2b400/public)

```text
Input: root = [1,2,3,null,null,4]

Output: true
```

**Example 2:**

![Example 2](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/24fcc2da-e012-4f9e-856e-040f200f3c00/public)

```text
Input: root = [1,2,3,null,null,4,null,5]

Output: false
```

**Example 3:**
```text
Input: root = []

Output: true
```

**Constraints:**
```text
The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
```

## 2. My Approach
```text
Let's break this problem down. What am I actually trying to do?
I'm trying to verify if a binary tree is height-balanced or not,
which means that for every node, its two subtrees only differ
in depth by no more than 1.

What does this mean? It means I need to first find a way to find
the depth of both of the subtrees given a root node. I already 
know how to do this recursively by just calling dfs on a root
node's children and traversing through both paths with the base
case being once I reach a node at the bottom that has non-existent
child nodes. I just return one added to the recursive call to track
how many nodes I visit.

Here's the twist with this problem: I need to find a way to verify
if the differences in depths of the two subtrees is no more than 1
to see if the tree is height balanced. So, I need an extra flag to 
check this. How about, if this condition is satisfied, I'll return
the actual height of the subtree, but then return -1 if it's not balanced.

Then, at the end, I can just return true or false based on if the final
return value from the dfs is a valid height or -1, respectively.

How do I actually implement this?
1. I define a dfs function
2. I define my base case (if not node: return 0)
3. I run the dfs on the left and right nodes to 
find the depths of those subtrees
4. I write a check to see if I found any imbalances along
the way down the tree. If so, I have to make sure I'm returning
-1 all the time since I already know the tree is imbalanced.
5. I write a check to see if the absolute value of the difference
between the depths of the two subtrees is greater than 1. If it is,
it's not balanced so I return -1.
6. Otherwise, I return the actual height of the subtree.
7. At the end, outside the dfs function, I call the dfs function on 
the root node and check if it's value is -1 or not. If it is, I return
false. If not, I return true.
```

