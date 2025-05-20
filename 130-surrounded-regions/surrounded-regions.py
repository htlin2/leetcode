class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c, mark, skip_mark=None):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return
            if grid[r][c] == 'X' or grid[r][c] == mark: return
            if skip_mark and grid[r][c] == skip_mark: return
            grid[r][c] = mark
            for dr, dc in directions:
                dfs(dr + r, dc + c, mark, skip_mark)
            return
        # convert edge O to *
        for r in range(ROWS):
            dfs(r, 0, '*')
            dfs(r, COLS - 1, '*')
        for c in range(COLS):
            dfs(0, c, '*')
            dfs(ROWS - 1, c, '*')

        # convert middle O to x
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                dfs(r, c, 'X', '*')

        # convert all * to O
        for r in range(ROWS):
            dfs(r, 0, 'O')
            dfs(r, COLS - 1, 'O')

        for c in range(COLS):
            dfs(0, c, 'O')
            dfs(ROWS - 1, c, 'O')