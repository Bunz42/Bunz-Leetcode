# 50 - Subtree of Another Tree

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/subtree-of-a-binary-tree/question

## 1. Problem Description
```text
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with
the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
```

**Example 1:**

<img width="636" height="523" alt="image" src="https://github.com/user-attachments/assets/4b7535a6-c05c-4488-8340-1a0e1b0c3cc7" />

```text
Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true
```

**Example 2:**

<img width="654" height="630" alt="image" src="https://github.com/user-attachments/assets/f7ffd0ec-f587-47b7-baa7-64582e660580" />

```text
Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false
```

**Constraints:**
```text
1 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
```

## 2. My Approach
```text
This problem is literally just the same as the "same binary tree"
problem I did yesterday, except with a bit of a twist. This time,
I need to implement the "isSameTree" function but then run it on
every subtree in the main tree, with the tree I'm comparing it to
being the desired subtree.

So, let's start by implementing the sameTree function. To implement
this, I need to dfs through both trees simultaneously, comparing each
of their nodes at every recursive step. We look at the root node of
each subtree recursively and return true or false depending on whether
or not they're identical.

How do I actually implement this?
1. Say you have 2 trees with roots root and subRoot respectively
2. Base case: if not root and not subRoot then return true
3. If not root or not subRoot then return false
4. If root.val != subRoot.val then return false
5. return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
because you need both to be true to have them be identical.

Now that we've implemented this sameTree() function, we just need to run it on every subtree
in the tree, and if we ever hit a true return from the sameTree function, we can return true.
However, if we never do, we return false.

How do I implement this?
1. Base case: if not root: return false
2. if sameTree(root, subRoot): return true
3. return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
4. Note: put a check at the beginning for (if not subRoot: return true) edge case
```

