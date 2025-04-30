# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        prefix_hashmap = collections.defaultdict(int)
        prefix_hashmap[0] += 1
        res = 0
        def dfs(node, curr):
            nonlocal res
            if not node: return
            curr += node.val
            delta = curr - target
            res += prefix_hashmap[delta]
            prefix_hashmap[curr] += 1
            dfs(node.left, curr)
            dfs(node.right, curr)
            prefix_hashmap[curr] -= 1
        dfs(root, 0)
        return res