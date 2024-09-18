class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        pacific, atlantic = set(), set() # (r, c)
        def dfs(r, c, visited):
            if (r, c) in visited: return
            visited.add((r, c))
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if nei_r < 0 or nei_c < 0 or nei_r >= ROW or nei_c >= COL: continue
                if grid[nei_r][nei_c] >= grid[r][c]:
                    dfs(nei_r, nei_c, visited)
        for c in range(COL):
            dfs(0, c, pacific)
            dfs(ROW - 1, c, atlantic)
        for r in range(ROW):
            dfs(r, 0, pacific)
            dfs(r, COL - 1, atlantic)
        return pacific.intersection(atlantic)