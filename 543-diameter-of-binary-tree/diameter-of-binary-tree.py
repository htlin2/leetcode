# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans = max(ans, left + right)
            return max(left, right) + 1
        dfs(root)
        return ans

"""
postorder dfs
    211
  121   31
04  50

max(left, right) + 1 
max(left + right + 1)
"""