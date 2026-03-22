# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_seen):
            if not node:
                return 0
            
            if node.val >= max_seen:
                goods = 1
            else:
                goods = 0
            
            curr_max = max(max_seen, node.val)
            left_goods = dfs(node.left, curr_max)
            right_goods = dfs(node.right, curr_max)

            return goods + left_goods + right_goods
        
        return dfs(root, root.val)
