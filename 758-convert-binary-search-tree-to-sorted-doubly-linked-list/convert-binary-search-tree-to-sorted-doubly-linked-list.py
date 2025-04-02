"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        head = tail = None
        def dfs(node):
            nonlocal head
            nonlocal tail
            if not node: return
            dfs(node.left)
            new_node = Node(node.val)
            if not tail:
                head = new_node
            else:
                tail.right = new_node
                new_node.left = tail
            tail = new_node
            dfs(node.right)
        dfs(root)
        head.left, tail.right = tail, head
        return head