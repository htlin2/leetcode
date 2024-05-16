# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        is_valid = True
        # dfs postorder
        def dfs(node):
            nonlocal is_valid
            if not node: return 0
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            if abs(left - right) >= 2:
                is_valid = False
            return max(left, right)
        dfs(root)
        return is_valid