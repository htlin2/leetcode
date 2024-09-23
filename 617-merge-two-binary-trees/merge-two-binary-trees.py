# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> Optional[TreeNode]:
        if not A: return B
        if not B: return A
        if not A and not B: return None
        A_val = A.val if A else 0
        B_val = B.val if B else 0
        node = TreeNode(A_val + B_val)

        A_left_node = A.left if A else None
        B_left_node = B.left if B else None
        node.left = self.mergeTrees(A_left_node, B_left_node)

        A_right_node = A.right if A else None
        B_right_node = B.right if B else None
        node.right = self.mergeTrees(A_right_node, B_right_node)
        return node

"""
dfs preorder
base case:
    if not A: return B
    if not B: return A
    if not A and not B: return None
A = A.val if A else 0
B = B.val if B else 0
combined_node = A + B
combined_node.left = dfs(A.left, B.left)
combined_node.right = dfs(A.right, B.right)
return combined_node
"""