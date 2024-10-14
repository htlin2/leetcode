class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROW, COL = len(grid), len(grid[0])
        res = set() # tuple(temp)
        def dfs(r, c, base_r, base_c, temp):
            if r < 0 or c < 0 or r >= ROW or c >= COL: return 
            if grid[r][c] == 0: return 
            temp.append((r - base_r, c - base_c))
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(dr + r, dc + c, base_r, base_c, temp)
        for r in range(ROW):
            for c in range(COL):
                temp = []
                if grid[r][c]:
                    dfs(r, c, r, c, temp)
                    res.add(tuple(temp))
        return len(res)
"""
how to know if islands are identical?

"""