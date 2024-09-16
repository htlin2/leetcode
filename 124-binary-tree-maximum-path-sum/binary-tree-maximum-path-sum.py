# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1000
        def dfs(node):
            nonlocal res
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            combined = left + right + node.val
            res = max(res, combined, left + node.val, right + node.val, node.val)
            return max(left + node.val, right + node.val, node.val)
        v = dfs(root)
        return max(res, v)