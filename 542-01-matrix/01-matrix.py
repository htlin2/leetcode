class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: continue
                up = grid[r - 1][c] if r - 1 >= 0 else float('inf')
                left = grid[r][c - 1] if c - 1 >= 0 else float('inf')
                grid[r][c] = min(up, left) + 1
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if grid[r][c] == 0: continue
                down = grid[r + 1][c] if r + 1 < ROWS else float('inf')
                right = grid[r][c + 1] if c + 1 < COLS else float('inf')
                grid[r][c] = min(grid[r][c], min(down, right) + 1)
        return grid

"""
Input: mat = [
    [0,1,0],
    [1,1,1],
    [1,1,1]
]
mat = [
    [0,0,0],
    [0,1,0],
    [#,2,1]
]

Output: [[0,0,0],[0,1,0],[1,2,1]]

"""