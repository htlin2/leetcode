class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        copy_grid = [row.copy() for row in grid]
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for r in range(ROW):
            for c in range(COL):
                one, zero = 0, 0
                is_live = copy_grid[r][c] == 1
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or cc < 0 or rr >= ROW or cc >= COL:
                        continue
                    if copy_grid[rr][cc] == 1:
                        one += 1
                    else:
                        zero += 1
                if is_live and (one < 2 or one > 3):
                    grid[r][c] = 0
                elif is_live and (one == 2 or one == 3):
                    grid[r][c] = 1
                elif is_live and one > 3:
                    grid[r][c] = 0
                elif not is_live and one == 3:
                    grid[r][c] = 1
        return grid
"""
Input: grid = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]

mid: [
    [0,0,0],
    [?,0,+],
    [0,+,+],
    [0,?,0]
]

Output: [
    [0,0,0],
    [1,0,1],
    [0,1,1],
    [0,1,0]
]

"""