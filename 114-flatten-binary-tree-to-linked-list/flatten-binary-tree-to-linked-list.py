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
        if not root: return root
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        if left:
            root.right = left
            while left and left.right:
                left = left.right
            left.right = right
        root.left = None
        return root