# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not r1 and not r2: return None
        if r1 and not r2: return r1
        if not r1 and r2: return r2
        node = TreeNode(r1.val + r2.val)
        node.left = self.mergeTrees(r1.left, r2.left)
        node.right = self.mergeTrees(r1.right, r2.right)
        return node

"""
preorder dfs
only stop when both root have no nodes
"""