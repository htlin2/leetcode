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
        hashmap = {None: None} # original_node: copy_node
        q = collections.deque([node])
        hashmap[node] = Node(node.val)
        while q:
            n = q.popleft()
            copy_node = hashmap[n]
            for nei in n.neighbors:
                if not nei in hashmap:
                    hashmap[nei] = Node(nei.val)
                    q.append(nei)
                copy_node.neighbors.append(hashmap[nei])
        return hashmap[node]

"""
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
node: neighbors
   1: [2,4]
   2: [3,1]
   3: [4,2]
   4: [1, 3]

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
hashmap = {original_node: copy_node}
q = [2, node(1), 2, node(3)]
1: [2, 4]
loop through q
    get or create copy_node
        add copy_node to hashmap
    if nei:
        make sure nei havent been visited
        add nei to q
Time: O(n)
Space: O(n)
"""