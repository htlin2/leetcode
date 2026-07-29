"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        root = node
        hashmap = {} # node: copy_node
        hashmap[node] = Node(node.val)
        q = collections.deque([node])
        while q:
            node = q.popleft()
            copy_node = hashmap[node]
            for nei in node.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                    q.append(nei)
                copy_node.neighbors.append(hashmap[nei])
        return hashmap[root]