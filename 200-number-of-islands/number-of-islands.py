class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0
        def bfs(r, c):
            q = collections.deque([[r, c]])
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    rr, cc = qr + dr, qc + dc
                    if rr < 0 or cc < 0 or rr >= ROWS or cc >= COLS: continue
                    if grid[rr][cc] == '0' or (rr, cc) in visited: continue
                    visited.add((rr, cc))
                    q.append([rr, cc])
            return
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0' or (r, c) in visited: continue
                visited.add((r, c))
                count += 1
                bfs(r, c)
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