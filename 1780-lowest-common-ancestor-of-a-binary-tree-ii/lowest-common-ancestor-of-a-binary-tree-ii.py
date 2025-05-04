# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        has_p, has_q = False, False
        def dfs(node):
            nonlocal has_p, has_q
            if not node: return node
            left = dfs(node.left)
            right = dfs(node.right)
            if node == p:
                has_p = True
                return node
            if node == q:
                has_q = True
                return node
            if left and right:
                return node
            return left or right
        res = dfs(root)
        return res if has_p and has_q else None