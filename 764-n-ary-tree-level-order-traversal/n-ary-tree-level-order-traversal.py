"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        hashmap = collections.defaultdict(list)
        def dfs(node, level):
            if not node: return
            hashmap[level].append(node.val)
            for child in node.children:
                dfs(child, level + 1)
            return
        dfs(root, 0)
        res = []
        for i in range(len(hashmap)):
            res.append(hashmap[i])
        return res