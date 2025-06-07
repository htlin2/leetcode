class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            adj[a].append((b, val))
            adj[b].append((a, 1/val))

        def bfs(src, dst):
            if src not in adj or dst not in adj:
                return -1
            visited = set([src])
            q = collections.deque([(src, 1)])
            while q:
                node, weight = q.popleft()
                if node == dst:
                    return weight
                for nei, nei_weight in adj[node]:
                    if nei not in adj: return -1
                    if nei in visited: continue
                    visited.add(nei)
                    q.append((nei, weight * nei_weight))
            return -1
        res = []
        for q1, q2 in queries:
            ans = bfs(q1, q2)
            res.append(ans)
        return res
"""
"""