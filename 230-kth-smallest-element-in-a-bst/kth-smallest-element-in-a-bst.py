# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        def preorder(node):
            if not node:
                return
            preorder(node.left)
            if len(nums) == k:
                return
            nums.append(node.val)
            preorder(node.right)
        preorder(root)
        return nums.pop()

"""
1. preorder dfs and get all node val + sort
Time: O(n log n)
Space: O(log n)

2. post-order dfs
left
right
node
1,2,
time: O(k)
space: O(n)
"""