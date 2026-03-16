# 49 - Same Binary Tree

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/balanced-binary-tree/question

## 1. Problem Description
```text
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
```

**Example 1:**

<img width="549" height="275" alt="image" src="https://github.com/user-attachments/assets/ac5ad370-4142-4ed4-a066-42296ad5129d" />

```text
Input: p = [1,2,3], q = [1,2,3]

Output: true
```

**Example 2:**

<img width="388" height="275" alt="image" src="https://github.com/user-attachments/assets/80784f19-227f-49b3-81cb-6aed6343f9ad" />

```text
Input: p = [4,7], q = [4,null,7]

Output: false
```

**Example 3:**

<img width="528" height="265" alt="image" src="https://github.com/user-attachments/assets/c4bb6065-0501-491f-b2ff-0a38a013d4e0" />

```text
Input: p = [1,2,3], q = [1,3,2]

Output: false
```

**Constraints:**
```text
0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
```

## 2. My Approach
```text
For this problem, you need to compare the two trees by searching
through them. So, I'm going to implement a dfs function.

I need to search through both trees simultaneously, starting from
their roots. At each step during the search, I will check to see 
if the node I'm currently looking at is equal to the corresponding
node in the other tree.

The base case will just be when both the nodes you're looking at
are nonexistent, since if the trees are in fact identical you'll 
always hit this condition at some point. At this point, you can just
return true.

Cases:
1. If one node is null and the other is not, return false
2. If both nodes exist but differ in value, return false
3. If the values of both nodes match then we continue running
the recursion down through their subtrees.
4. If any of the recursive calls return false then the output is
just false automatically.

How to implement:
- Define base case: both nodes are null, return true.
- Check if one is null and the other is not, return false.
- Check if the values at both nodes are not equal, return false.
- Run the recursive dfs on the child nodes of the tree
- Return dfs(subtree1) and dfs(subtree2) because both need to be
tree for the entire tree to be identical.
```

