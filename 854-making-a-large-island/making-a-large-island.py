class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        label_area = collections.defaultdict(int) # label: area
        def dfs(r, c, label):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return 0
            if grid[r][c] == 0 or grid[r][c] == label: return 0
            grid[r][c] = label
            res = 1
            for nr, nc in directions:
                res += dfs(nr + r, nc + c, label)
            return res
        label = 2
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c, label)
                    label_area[label] = area
                    label += 1

        if label_area:
            res = max(label_area.values())
        else:
            res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0: continue
                visited = set()
                curr_area = 1
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                    label = grid[nr][nc]
                    if label in visited: continue
                    curr_area += label_area[label]
                    visited.add(label)
                res = max(curr_area, res)
        return 1 if res == 0 else res