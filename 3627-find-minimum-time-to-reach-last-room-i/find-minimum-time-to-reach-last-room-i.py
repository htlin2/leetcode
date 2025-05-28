class Solution:
    def minTimeToReach(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [(0, 0, 0)] # time_, r, c
        visited = set()
        while min_heap:
            time_, r, c = heapq.heappop(min_heap)
            if r == ROWS - 1 and c == COLS - 1:
                return time_
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue
                if (nr, nc) in visited:
                    continue
                new_time = max(time_, grid[nr][nc]) + 1
                heapq.heappush(min_heap, (new_time, nr, nc))
        return -1