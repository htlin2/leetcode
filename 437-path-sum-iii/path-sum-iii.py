# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        path_count = collections.defaultdict(int) # path_sum: count
        path_count[0] = 1
        res = 0
        def dfs(node, curr_sum):
            nonlocal res
            if not node: return
            curr_sum += node.val
            delta = curr_sum - target
            res += path_count[delta]
            path_count[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            path_count[curr_sum] -= 1
            return
        dfs(root, 0)
        return res
"""
preorder dfs
store all accumulated path
subtract to get current path sum
"""