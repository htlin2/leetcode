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
        hashmap = {None: None} # original_node: copy_node
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            copy_node = Node(node.val)
            hashmap[node] = copy_node
            for nei in node.neighbors:
                nei_copy_node = dfs(nei)
                copy_node.neighbors.append(nei_copy_node)
            return copy_node
        dfs(node)
        return hashmap[node]

"""
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
hashmap = {
    original_node: copy_node
}
1. dfs(node):
    if node in hashmap:
        return copy_node
    if not in hashmap
        create new copy_node and save in hashmap
    loop through nei
        copy_nei_node = call dfs(nei_node)
        append copy_nei_node to copy_node

Time: O(n)
Space: O(n)

2. bfs
add adj nodes to q
loop through q
    get or create copy_node
    add copy_node to nei
Time: O(n)
Space: O(n)
"""