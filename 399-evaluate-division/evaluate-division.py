class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # a: (b, val)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            adj[a].append([b, val])
            adj[b].append([a, 1 / val])
        
        def bfs(src, dst):
            if src not in adj or dst not in adj: return -1
            visited = set()
            q = collections.deque([[src, 1]])
            while q:
                node, val = q.popleft()
                if node == dst: return val
                for nei, nei_val in adj[node]:
                    if nei in visited: continue
                    visited.add(nei)
                    q.append([nei, nei_val * val])
            return -1

        res = []
        for q1, q2 in queries:
            res.append(bfs(q1, q2))
        
        return res