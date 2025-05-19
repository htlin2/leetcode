class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # a: [b, val]
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            adj[a].append((b, val))
            adj[b].append((a, 1 / val))
        res = []
        def dfs(src, dst, weight, visited):
            if src in visited: return -1
            if src == dst: return weight
            visited.add(src)
            for nei, nei_weight in adj[src]:
                res = dfs(nei, dst, weight * nei_weight, visited)
                if res != -1:
                    return res
            return -1

        for q1, q2 in queries:
            if q1 not in adj or q2 not in adj:
                res.append(-1)
                continue
            res.append(dfs(q1, q2, 1, set()))
        return res