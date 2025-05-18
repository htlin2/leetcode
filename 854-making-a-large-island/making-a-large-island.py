class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        island_size = collections.defaultdict(int) # label: island_size
        label = 2
        def dfs(r, c, label):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return 0
            if grid[r][c] == 0 or grid[r][c] == label: return 0
            grid[r][c] = label
            res = 1
            for dr, dc in directions:
                res += dfs(dr + r, dc + c, label)
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    island_size[label] = dfs(r, c, label)
                    label += 1

        res = 0 if not island_size else max(island_size.values())
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0: continue
                curr_size = 1
                visited_labels = set()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                    label = grid[nr][nc]
                    if label in visited_labels: continue
                    visited_labels.add(label)
                    curr_size += island_size[label]
                res = max(res, curr_size)
        return res
"""
Input: grid = [
    [1,1],
    [0,1]
]

"""