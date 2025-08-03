# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            curr_max = max(left + right + node.val, left + node.val, right + node.val)
            res = max(res, curr_max, node.val)
            return max(max(left, right) + node.val, node.val)
        dfs(root)
        return res

"""
postorder dfs

"""