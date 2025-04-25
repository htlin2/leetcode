# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # Initialize with 0:1 to handle paths starting from the root

        def dfs(node, current_sum):
            nonlocal count
            if not node: return

            current_sum += node.val
            # Check if there's a previous prefix sum such that (current_sum - previous_sum) == targetSum
            if (current_sum - targetSum) in prefix_sum:
                count += prefix_sum[current_sum - targetSum]

            prefix_sum[current_sum] += 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Backtrack: remove the current sum from the prefix sum count as we go up
            prefix_sum[current_sum] -= 1

        dfs(root, 0)
        return count
