class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        original_color = grid[sr][sc]
        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0:
                return
            if grid[r][c] != original_color or grid[r][c] == color:
                return
            grid[r][c] = color
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return
        dfs(sr, sc)
        return grid