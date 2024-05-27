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
        hashmap = {} # node: cloned
        def dfs(node):
            if node in hashmap: return hashmap[node]
            hashmap[node] = Node(node.val)
            for nei in node.neighbors:
                cloned = dfs(nei)
                hashmap[node].neighbors.append(cloned)
            return hashmap[node]
        return dfs(node)