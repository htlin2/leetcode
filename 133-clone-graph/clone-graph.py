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
        visited, node_cloned = set(), {}
        def dfs(node):
            # base case: if node in visited: return
            if node in node_cloned: return node_cloned[node]
            node_cloned[node] = Node(node.val)
            # iterate through neighbors of original node:
            for nei in node.neighbors:
                # recersively call dfs(nei)
                node_cloned[node].neighbors.append(dfs(nei))
            return node_cloned[node]
        dfs(node)
        return node_cloned[node]

"""
dfs + hashmap
node_cloned = {
    node: cloned_node
}

"""