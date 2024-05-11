# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
"""
q = []
while q:
    iterate through q:
        swap left and right
        if left:
            append left to q
        if right:
            append right to q
return root
"""