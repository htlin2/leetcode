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
        if not node: return node
        hashmap = {}
        hashmap[node] = Node(node.val)
        q = collections.deque([node])
        while q:
            first = q.popleft()
            for nei in first.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                    q.append(nei)
                hashmap[first].neighbors.append(hashmap[nei])
        return hashmap[node]