# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root: return []
        adj = collections.defaultdict(set)
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    adj[node.val].add(node.left.val)
                    adj[node.left.val].add(node.val)
                    q.append(node.left)
                if node.right:
                    adj[node.val].add(node.right.val)
                    adj[node.right.val].add(node.val)
                    q.append(node.right)
        visited = set()
        res = []
        def dfs(val, level):
            if val in visited: return
            visited.add(val)
            if level == k:
                res.append(val)
                return
            for nei in adj[val]:
                dfs(nei, level + 1)
        dfs(target.val, 0)
        return res