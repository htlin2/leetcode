"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# 1 -> 2 -> 3 -> 4 -> 5
class Solution:
    def treeToDoublyList(self, root):
        if not root: return root
        head = curr = ListNode(-1)
        def dfs(node):
            nonlocal head
            nonlocal curr
            if not node: return
            dfs(node.left)
            # inorder
            # build LL
            ll_node = Node(node.val) # 2
            curr.right = ll_node # 1 -> 2
            left = curr # left = 1
            curr = curr.right # curr = 2
            curr.left = left # 1 <-> 2
            dfs(node.right)
        dfs(root)
        head = head.right
        head.left = curr
        curr.right = head
        return head