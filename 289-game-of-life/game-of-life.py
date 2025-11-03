class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        copy_grid = [row.copy() for row in grid]
        for r in range(ROWS):
            for c in range(COLS):
                counts = 0
                for dr, dc in directions:
                    rr, cc = dr + r, dc + c
                    if rr < 0 or cc < 0 or rr >= ROWS or cc >= COLS:
                        continue
                    counts += copy_grid[rr][cc]
                is_live = copy_grid[r][c]
                if is_live and counts < 2:
                    grid[r][c] = 0
                elif is_live and counts in [2, 3]:
                    grid[r][c] = 1
                elif is_live and counts > 3:
                    grid[r][c] = 0
                elif not is_live and counts == 3:
                    grid[r][c] = 1
        return