# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] += 1
        res = 0
        def dfs(node, curr):
            nonlocal res
            if not node: return
            curr += node.val
            delta = curr - t
            res += prefix[delta]
            prefix[curr] += 1
            dfs(node.left, curr)
            dfs(node.right, curr)
            prefix[curr] -= 1
            return
        dfs(root, 0)
        return res