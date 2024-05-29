class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return
            if grid[r][c] == '0': return
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0': continue
                count += 1
                dfs(r, c)
        return count

"""
1 DFS
iterate through grid
run dfs on 1
    increment count
    iterate through 4 directions
    check for out of bounds
    mark 1 to 0
    call dfs on 4 directions
return count

2 BFS
iterate through grid
when hitting 1 
increment count
run BFS
    iterate through 4 directions
    mark 1's to 0's
return count

3 Union Find
iterate through grid
    when hittin 1
    iterate through 4 directions
        union with original 1 from grid
        count how many successful unions
return R*C - successful unions
"""