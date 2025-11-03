class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        {
            b,a
            0,0: 0
            1,0: 1
            0,1: 2
            1,1: 3
        }
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                counts = 0
                is_live = grid[r][c]
                for dr, dc in directions:
                    rr, cc = dr + r, dc + c
                    if rr < 0 or cc < 0 or rr >= ROWS or cc >= COLS:
                        continue
                    key = grid[rr][cc]
                    if key in [1, 3]:
                        counts += 1
                if is_live and counts < 2:
                    grid[r][c] = 1
                elif is_live and counts in [2, 3]:
                    grid[r][c] = 3
                elif is_live and counts > 3:
                    grid[r][c] = 1
                elif not is_live and counts == 3:
                    grid[r][c] = 2
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in [0, 1]:
                    grid[r][c] = 0
                elif grid[r][c] in [2,3]:
                    grid[r][c] = 1
        return