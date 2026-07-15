# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = collections.deque([root])
        res = []
        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr_level)
        return res
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