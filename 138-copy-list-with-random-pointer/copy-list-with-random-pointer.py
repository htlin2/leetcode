"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None} # original_node: copy_node
        node = head
        while node:
            copy_node = Node(node.val)
            hashmap[node] = copy_node
            node = node.next
        node = head
        while node:
            copy_node = hashmap[node]
            next_node = hashmap[node.next]
            random_node = hashmap[node.random]
            copy_node.next, copy_node.random = next_node, random_node
            node = node.next
        return hashmap[head]