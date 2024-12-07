# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p and q: return False
        if p and not q: return False
        if p.val == q.val and self.is_same(p, q):
            return True
        return self.isSubtree(p.left, q) or self.isSubtree(p.right, q)

    def is_same(self, p, q):
        if not p and not q: return True
        if not p and q: return False
        if p and not q: return False
        if p.val != q.val: return False
        return self.is_same(p.left, q.left) and self.is_same(p.right, q.right)
"""
dfs preorder
"""