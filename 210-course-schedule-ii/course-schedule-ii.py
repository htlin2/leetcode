class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
        res, visited = [], set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visited.add(node)
            res.append(node)
            cycle.remove(node)
            return True
        for node in range(N):
            if node in visited:
                continue
            if not dfs(node):
                return []
        return [] if len(res) != N else res[::-1]
"""
graph
"""