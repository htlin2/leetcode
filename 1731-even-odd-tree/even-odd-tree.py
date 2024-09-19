# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        q = collections.deque([root])
        level = -1
        while q:
            level += 1
            is_even = True if level % 2 == 0 else False
            prev_val = float('-inf') if is_even else float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                if is_even:
                    # odd node.val
                    if not (node.val % 2 == 1):
                        return False
                    # increasing order (from left to right)
                    if not (prev_val < node.val):
                        return False
                else:
                    # even node.val
                    if not (node.val % 2 == 0):
                        return False
                    # decreasing order (from left to right)
                    if not (node.val < prev_val):
                        return False
                prev_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return True
                