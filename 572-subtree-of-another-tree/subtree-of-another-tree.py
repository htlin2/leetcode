# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, root, subRoot):
        # post-order
        if not root and not subRoot: return True
        if root and not subRoot: return False
        if not root and subRoot: return False
        if root.val != subRoot.val: return False
        left = self.isSame(root.left, subRoot.left)
        right = self.isSame(root.right, subRoot.right)
        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # pre-order dfs
        # base case: 
        if not root and not subRoot: return True
        if root and not subRoot: return False
        if not root and subRoot: return False
        # when do i go to next level?
        if root.val == subRoot.val and self.isSame(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
        # if left and right are true: return True
        # else return False
        return left or right
