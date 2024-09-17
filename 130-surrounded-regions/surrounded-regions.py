class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # (r, c)
        ROW, COL = len(grid), len(grid[0])
        for c in range(COL):
            if grid[0][c] == 'O':
                grid[0][c] = '#'
            if grid[ROW - 1][c] == 'O':
                grid[ROW - 1][c] = '#'
        for r in range(ROW):
            if grid[r][0] == 'O':
                grid[r][0] = '#'
            if grid[r][COL - 1] == 'O':
                grid[r][COL - 1] = '#'
        def dfs(r, c, o_coordinates):
            if grid[r][c] == 'X':
                return True
            if (r, c) in o_coordinates:
                return True
            if grid[r][c] == '#':
                return False
            o_coordinates.add((r, c))
            res = True
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if nei_r < 0 or nei_c < 0 or nei_r >= ROW or nei_c >= COL:
                    continue
                res = res and dfs(nei_r, nei_c, o_coordinates)
            return res
        for r in range(ROW):
            for c in range(COL):
                o_coordinates = set()
                if not dfs(r, c, o_coordinates): continue
                for coor_r, coor_c in o_coordinates:
                    grid[coor_r][coor_c] = 'X'

        for c in range(COL):
            if grid[0][c] == '#':
                grid[0][c] = 'O'
            if grid[ROW - 1][c] == '#':
                grid[ROW - 1][c] = 'O'
        for r in range(ROW):
            if grid[r][0] == '#':
                grid[r][0] = 'O'
            if grid[r][COL - 1] == '#':
                grid[r][COL - 1] = 'O'
"""
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","#","X","X"]

DFS to find all O's coordinates
    if curr cell is X: return True
    if curr cell has been visited: return True
    if curr cell is O:
        keep track of O to O_coordinates
    loop through 4 directions:
        check out of bound, skip
        call dfs() with next direction
        make sure all 4 directions are True
    return True if all surround by X, else False

loop through all cells in grid:
    call DFS(row, col, o_coordinates)
    if above is true
    loop through o_coordinates to replace O with X

replace all '#' with 'O'
"""