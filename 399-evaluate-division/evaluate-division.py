class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(set) #
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            adj[a].add((b, val))
            adj[b].add((a, 1 / val))
        res = []

        def dfs(src, dst, weight, visited):
            if src == dst: return weight
            visited.add(src)
            for nei_src, nei_weight in adj[src]:
                if nei_src in visited: continue
                res = dfs(nei_src, dst, weight * nei_weight, visited)
                if res != -1:
                    return res
            return -1
        for q1, q2 in queries:
            if q1 not in adj or q2 not in adj:
                res.append(-1)
            else:
                res.append(dfs(q1, q2, 1, set()))
        return res