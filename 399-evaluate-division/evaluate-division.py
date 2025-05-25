class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # a: (b, val)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            adj[a].append((b, val))
            adj[b].append((a, 1 / val))
        def bfs(src, dst):
            if src not in adj or dst not in adj: return -1
            q = collections.deque()
            q.append((src, 1))
            visited = set([src])
            while q:
                first, weight = q.popleft()
                if first == dst: return weight
                visited.add(first)
                for nei_src, nei_weight in adj[first]:
                    if nei_src in visited: continue
                    q.append((nei_src, weight * nei_weight))
            return -1
        
        res = []
        for q1, q2 in queries:
            ans = bfs(q1, q2)
            res.append(ans)
        return res