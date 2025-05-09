class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        adj = collections.defaultdict(set)
        for r in range(len(grid)):
            for c in range(r + 1, len(grid)):
                if grid[r][c]:
                    adj[r].add(c)
                    adj[c].add(r)
        visited = set()
        def dfs(i):
            if i in visited: return
            visited.add(i)
            for nei in adj[i]:
                dfs(nei)
            return
        res = 0
        for i in range(len(grid)):
            if i not in visited:
                dfs(i)
                res += 1
        return res