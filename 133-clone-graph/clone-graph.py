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

        hashmap = {} # node: copy_node
        def dfs(node):
            if node in hashmap: return hashmap[node]
            hashmap[node] = Node(node.val)
            for nei in node.neighbors:
                hashmap[node].neighbors.append(dfs(nei))
            return hashmap[node]
        dfs(node)
        return hashmap[node]
"""
1: [2,4]
2: [1,3]
3: [2,4]
4: [1,3]

dup
1: 1_d
2: 2_d

"""