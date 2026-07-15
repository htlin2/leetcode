# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        hashmap = collections.defaultdict(list)
        def dfs(node, curr_level):
            if not node: return
            hashmap[curr_level].append(node.val)
            if node.left:
                dfs(node.left, curr_level + 1)
            if node.right:
                dfs(node.right, curr_level + 1)
        dfs(root, 0)
        return list(hashmap.values())
"""
1. dfs
when go down to each level track the curr_level
add to hashmap: {curr_level: [lists]}


2. bfs
queue
while queue
    curr_level
    for in range(len(queue))
        pop queue
        push to curr_level
        add left, right tree nodes to queue + handle None
    append curr_level to res
T:O(n)
S:O(n)
"""