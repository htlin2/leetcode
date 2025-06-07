class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            adj[a].append((b, val))
            adj[b].append((a, 1/val))

        def dfs(src, dst, visited, weight):
            if src not in adj or dst not in adj: return -1
            if src == dst: return weight
            if src in visited: return -1
            visited.add(src)
            for nei, nei_weight in adj[src]:
                if nei in visited: continue
                res = dfs(nei, dst, visited, weight * nei_weight)
                if res != -1: return res
            return -1

        res = []
        for q1, q2 in queries:
            ans = dfs(q1, q2, set(), 1)
            res.append(ans)
        return res
"""
"""