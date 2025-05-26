class Solution:
    def canFinish(self, N: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(set)
        for src, dst in prerequisites:
            adj[src].add(dst)
        visited, cycle = set(), set()
        res = set()
        def dfs(src):
            if src in visited: return True
            if src in cycle: return False
            cycle.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            visited.add(src)
            cycle.remove(src)
            return True
        for i in range(N):
            if not dfs(i):
                return False
        return len(visited) == N