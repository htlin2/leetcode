# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1
        res = 0
        def dfs(node, curr_sum):
            nonlocal res
            if not node: return
            curr_sum += node.val
            delta = curr_sum - target_sum
            res += hashmap[delta]
            hashmap[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            hashmap[curr_sum] -= 1
        dfs(root, 0)
        return res