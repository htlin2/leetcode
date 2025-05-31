class Solution:
    def minTimeToReach(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [(0, 0, 0, 2)] # time_, r, c, alt
        visited = set()
        while min_heap:
            time_, r, c, alt = heapq.heappop(min_heap)
            if r == ROWS - 1 and c == COLS - 1: return time_
            if (r, c, alt) in visited: continue
            visited.add((r, c, alt))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                new_alt = 1 if alt == 2 else 2
                if (nr, nc, new_alt) in visited: continue
                new_time = max(time_, grid[nr][nc]) + new_alt
                heapq.heappush(min_heap, (new_time, nr, nc, new_alt))
        return -1