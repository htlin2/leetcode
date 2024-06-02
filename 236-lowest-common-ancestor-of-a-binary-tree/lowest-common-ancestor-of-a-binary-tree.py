# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return node
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == p.val or node.val == q.val: return node
            if left and right: return node
            if left: return left
            if right: return right
            return None
        return dfs(root)
        
"""
DFS postorder



"""