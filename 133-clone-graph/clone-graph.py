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
        hashmap, visited = {}, set()
        q = collections.deque([node])
        while q:
            first = q.popleft()
            if first in visited: continue
            visited.add(first)
            if first not in hashmap:
                hashmap[first] = Node(first.val)
            for nei in first.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                cloned_nei_node = hashmap[nei]
                hashmap[first].neighbors.append(cloned_nei_node)
                if nei in visited: continue
                q.append(nei)
        return hashmap[node]
"""
linkedlist + hashmap
1. bfs - iteratively
hashmap = {node: copy_node}
q = deque([node])
while q:
    first = q.pop()
    if first == node: break
    cloned_node = Node(first)
    if first not in hashmap:
        hashmap[first] = cloned_node
    else:
        cloned_node = hashmap[first]
    iterate through first's neighbors
        cloned_nei_node = Node(nei)
        if neighbor not in hashmap:
            hashmap[nei] = cloned_nei_node
        else;
            cloned_nei_node = hashmap[nei]
        cloned_node.neighbors.append(cloned_nei_node)
return hashmap[node]

2. dfs- recurrsion
    def dfs(node):
        base case: if node in hashmap: return node
    
"""