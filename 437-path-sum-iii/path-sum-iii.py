# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        memo = collections.defaultdict(int)
        memo[0] = 1
        res = 0
        def dfs(node, memo, curr_sum):
            nonlocal res
            if not node: return
            curr_sum += node.val
            delta = curr_sum - target
            res += memo[delta]
            memo[curr_sum] += 1
            dfs(node.left, memo, curr_sum)
            dfs(node.right, memo, curr_sum)
            memo[curr_sum] -= 1
        dfs(root, memo, 0)
        return res
"""
prefix sum
{
    10: 1
    15: 1
    17: 1
    18: 1
}
"""