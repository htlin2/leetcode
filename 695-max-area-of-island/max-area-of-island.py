class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            grid[r][c] = 0
            res = 0
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                if grid[nr][nc] == 0: continue
                res += dfs(nr, nc) + 1
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c) + 1)
        return res