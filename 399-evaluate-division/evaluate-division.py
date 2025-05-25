class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # a: (b, val)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            adj[a].append((b, val))
            adj[b].append((a, 1 / val))

        def dfs(src, dst, weight, visited):
            if src not in adj or dst not in adj: return -1
            if src == dst: return weight
            for nei_src, nei_weight in adj[src]:
                if nei_src in visited: continue
                visited.add(nei_src)
                ans = dfs(nei_src, dst, weight * nei_weight, visited)
                if ans != -1:
                    return ans
            return -1

        res = []
        for q1, q2 in queries:
            visited = set()
            res.append(dfs(q1, q2, 1, visited))
        return res