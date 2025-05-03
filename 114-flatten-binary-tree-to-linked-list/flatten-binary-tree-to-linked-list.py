# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def dfs(node):
            nonlocal prev
            if not node: return node
            dfs(node.right)
            dfs(node.left)
            node.right = prev
            prev = node
            node.left = None
        dfs(root)
        return prev