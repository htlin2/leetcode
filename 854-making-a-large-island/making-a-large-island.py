class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        id_ = 2
        memo = collections.defaultdict(int) # id_: total_area
        def dfs(r, c, id_):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return 0
            if grid[r][c] != 1: return 0
            grid[r][c] = id_
            res = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                res += dfs(nr, nc, id_)
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 1: continue
                area = dfs(r, c, id_)
                memo[id_] = area
                id_ += 1
        if memo:
            res = max(memo.values())
        else:
            res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0: continue
                curr_area = 1
                visited_id = set()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                    n_id = grid[nr][nc]
                    if n_id in visited_id: continue
                    visited_id.add(n_id)
                    curr_area += memo[n_id]
                res = max(res, curr_area)
        return res