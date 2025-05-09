class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(set)
        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)
        visited = set()
        def has_cycle(node, prev):
            if node in visited: return True
            visited.add(node)
            for nei in adj[node]:
                if nei == prev: continue
                if has_cycle(nei, node):
                    return True
            return False
        if has_cycle(0, -1):
            return False
        return len(visited) == n