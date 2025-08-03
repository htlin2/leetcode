# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = collections.defaultdict(set)
        def build_adj(node):
            if not node: return
            left = node.left
            right = node.right
            if left:
                adj[node.val].add(left.val)
                adj[left.val].add(node.val)
            if right:
                adj[node.val].add(right.val)
                adj[right.val].add(node.val)
            build_adj(node.left)
            build_adj(node.right)
            return
        build_adj(root)
        visited = set()
        res = []
        def dfs(val, count):
            if val in visited: return
            visited.add(val)
            if not count:
                res.append(val)
                return
            for nei in adj[val]:
                dfs(nei, count - 1)
            return
        dfs(target.val, k)
        return res
"""
graph + dfs
3: [5, 1]
5: [3, 2, 6]
6: [5]
2: [6, 7, 4]
1: [3, 0, 8]


"""