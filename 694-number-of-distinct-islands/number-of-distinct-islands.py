class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = set() # islands tuples
        def dfs(r, c, org_r, org_c, islands):
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            islands.append((r - org_r, c - org_c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, org_r, org_c, islands)
        for r in range(ROW):
            for c in range(COL):
                islands = []
                if grid[r][c] == 1:
                    dfs(r, c, r, c, islands)
                    res.add(tuple(islands))
        return len(res)
"""
DFS + regonize islands that are duplicates
Input: grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]
Output: 1
dfs(r, c, org_r, org_c):
    islands.append((r - org_r, c - org_c))
    tuple(islands) and store in result(set)
"""