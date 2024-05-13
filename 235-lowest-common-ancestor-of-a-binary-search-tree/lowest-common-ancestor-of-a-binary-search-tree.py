# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # swap p <> q, so p is always smaller than q
        if p.val >= q.val:
            return self.lowestCommonAncestor(root, q, p)
        # preorder dfs
        # base case:
        if not root: return root
        if p.val <= root.val <= q.val: return root
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)