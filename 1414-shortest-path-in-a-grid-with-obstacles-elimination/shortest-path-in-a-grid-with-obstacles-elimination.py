class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = [(0, 0, 0, k)] # weight, r, c, rem_k
        visited = set() # (r, c, rem_k)
        while min_heap:
            weight, r, c, rem_k = heapq.heappop(min_heap)
            if r == ROWS - 1 and c == COLS - 1:
                return weight
            if (r, c, rem_k) in visited: continue
            visited.add((r, c, rem_k))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                if (nr, nc, rem_k) in visited: continue
                if grid[nr][nc] == 1 and rem_k:
                    heapq.heappush(min_heap, (weight + 1, nr, nc, rem_k - 1))
                elif grid[nr][nc] == 0:
                    heapq.heappush(min_heap, (weight + 1, nr, nc, rem_k))
        return -1