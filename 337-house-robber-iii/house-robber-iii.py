# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = collections.defaultdict(int)
        def dfs(node, skip):
            if not node: return 0
            if (node, skip) in memo: return memo[node, skip]
            if skip:
                memo[node, skip] = dfs(node.left, False) + dfs(node.right, False)
                return memo[node, skip]
            add_sum = dfs(node.left, True) + dfs(node.right, True) + node.val
            skip_sum = dfs(node.left, False) + dfs(node.right, False)
            memo[node, skip] = max(add_sum, skip_sum)
            return memo[node, skip]
        return dfs(root, False)
"""
graph
3: [4, 5]
4: [1, 3]
1: []
3: []
5: [1]
"""