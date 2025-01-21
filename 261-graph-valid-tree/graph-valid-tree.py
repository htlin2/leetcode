class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list) # src: [dst]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        if not dfs(0, None):
            return False
        return True if len(visited) == n else False