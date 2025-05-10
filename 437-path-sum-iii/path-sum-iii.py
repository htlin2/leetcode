# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        res = 0
        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] = 1
        def dfs(node, curr_sum):
            nonlocal res
            if not node: return
            curr_sum += node.val
            delta = curr_sum - target
            res += prefix_sum[delta]
            prefix_sum[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix_sum[curr_sum] -= 1
        dfs(root, 0)
        return res