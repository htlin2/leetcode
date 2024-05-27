# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(node, left, right):
            nonlocal ans
            if ans == False: return
            if not node: return
            if not (left < node.val < right):
                ans = False
                return
            dfs(node.left, left, min(node.val, right))
            dfs(node.right, max(node.val, left), right)
        dfs(root, float('-inf'), float('inf'))
        return ans

"""
DFS - postorder

"""