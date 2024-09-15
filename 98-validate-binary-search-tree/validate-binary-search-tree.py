# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = float('-inf'), right = float('inf')) -> bool:
        if not root: return True
        if not (left < root.val < right): return False
        left_tree = self.isValidBST(root.left, left, root.val)
        right_tree = self.isValidBST(root.right, root.val, right)
        return left_tree and right_tree
"""
preorder dfs
"""