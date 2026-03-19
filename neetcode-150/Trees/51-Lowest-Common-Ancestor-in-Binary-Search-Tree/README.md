# 51 - Lowest Common Ancestor in Binary Search Tree

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree/question

## 1. Problem Description
```text
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q,
return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants.
The ancestor is allowed to be a descendant of itself.
```

**Example 1:**

<img width="536" height="402" alt="image" src="https://github.com/user-attachments/assets/d03ebc57-bf0f-4db4-bacc-eadecc8ebbd2" />

```text
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
```

**Example 2:**

<img width="536" height="402" alt="image" src="https://github.com/user-attachments/assets/88490061-395e-4a11-9d32-6e61ec5df834" />

```text
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

Output: 3

Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.
```

**Constraints:**
```text
2 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST.
```

## 2. My Approach
```text
In this problem, I'm not working with just a regular binary tree like I was in the previous
tree problems. This time, I'm working with a binary search tree (BST). So, this means I don't
need to get fancy with complex DFS where I check every node and backtrack answers. I can just
solve it by following the rules of a BST.

Rules:
1. Everything in the left branch is strictly smaller
2. Everything in the right branch is strictly larger

So, this basically allows me to search through the tree in the same way I would binary search
through an array, hence the name "binary search tree". I just ask, "is my target bigger or
smaller than the current node value?" Then I move left or right accordingly.

To find the lowest common ancestor (LCA) of two nodes. I'm going to imagine dropping the two
nodes in from the very top of the tree at the same time. By the rules of BST, the two nodes
p and q are just going to follow the same path until they hit the LCA, which is just the node
where they need to split up.

So, I just need to check 3 scenarios at whatever node I'm looking at right now:
1. p and q both go right: if p and q are both strictly greater than the current node, then the
LCA has to be down the right branch, so we move down the right.

2. Both go left: if p and q are both strictly smaller than the current node, the LCA has to be
in the left branch, so we move down the left.

3. Split: if one goes left and one goes right, or if one of them is equal to the current node,
then I found the LCA, so I can just return that value.

Implementation:
1. curr = root
2. while curr exists
3. if p.val > curr.val and q.val > curr.val: move right
4. elif p.val < curr.val and q.val < curr.val: move left
5. else: return curr

Note: this solution is O(h) time complexity where h is the height of the tree, since I'm iterating
at most through the height of the binary search tree if the LCA were to be located at the bottom of 
the deepest path.
```

