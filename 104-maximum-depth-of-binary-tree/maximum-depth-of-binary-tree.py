# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        def dfs(node):
            nonlocal res
            if not node: return 0
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            res = max(res, left, right)
            return max(left, right)
        dfs(root)
        return res
        
        
"""
postorder dfs or BFS

"""