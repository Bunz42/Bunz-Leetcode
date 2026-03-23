# 54 - Count Good Nodes in Binary Tree

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/count-good-nodes-in-binary-tree/question

## 1. Problem Description
```text
Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains
no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.
```

**Example 1:**

<img width="625" height="345" alt="image" src="https://github.com/user-attachments/assets/2d589597-f9b7-454b-84f2-ea8fbfa8ac8a" />

```text
Input: root = [2,1,1,3,null,1,5]

Output: 3
```

**Example 2:**

<img width="274" height="344" alt="image" src="https://github.com/user-attachments/assets/1d422bc3-becb-4cc5-a2ef-c6fb5b7c20aa" />

```text
Input: root = [1,2,-1,3,4]

Output: 4
```

**Constraints:**
```text
1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
```

## 2. My Approach
```text
You can brute force this problem by simply looking at every node in the tree and 
checking if the path from the root to that node is valid. However, this would result
in an O(n^2) time complexity because you need to iterate through each node once and
also iterate from the root to that given node during each iteration.

Instead, a better way to do this would be to use some variation of a depth first search (dfs).
The reason why I'm thinking of using dfs for this problem is because this problem cares about
traversing down single paths to validate them rather than traversing the tree level by level.

I'll determine whether or not a node is a good node by tracking the current maximum node seen
along the path so far. If the node I'm looking at is less than the current maximum node seen,
then it's not a good node. If a node is greater than or equal to the max seen so far, then it is 
a good node so we can increase the counter and update the max node variable.

Now, we just have to run this dfs variation on every path so we can find all the good nodes
along every path.

Implementation:
1. dfs helper function that takes in a node and a max value seen so far
2. if not node: return 0
3. if node.val >= max_seen: goods = 1
4. else: goods = 0
5. curr_max = max(max_seen, node.val)
6. left_goods = dfs(node.left, curr_max)
7. right_goods = dfs(node.right, curr_max)
8. return goods + left_goods + right_goods
9. (outside dfs helper) call dfs(root, root.val)

Brief explanation of implementation:
1: I need a helper function for the dfs because we need extra data (the max variable) to make
things work
2: Base case
3-4: Logic for identifying good node
5: Update the current max seen
6-7: Find the good nodes of the left and right subtrees using the new max
8: Return total number of good nodes (good node + its children's good nodes)
9: Call the dfs starting at the root node and passing in the root node's value as the max seen
(since it's the only node seen so far so it has to be the max)
```

