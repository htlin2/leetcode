class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [(0, 0, 0, k)] # (weight, r, c, rem_k)
        visited = set()
        visited.add((0, 0))
        while min_heap:
            weight, r, c, rem_k = heapq.heappop(min_heap)
            if r == ROWS - 1 and c == COLS - 1:
                return weight
            visited.add((r, c, rem_k))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                if grid[nr][nc] == 1 and rem_k == 0: continue
                new_k = rem_k - 1 if grid[nr][nc] == 1 else rem_k
                if (nr, nc, new_k) in visited: continue
                visited.add((nr, nc, new_k))
                heapq.heappush(min_heap, (weight + 1, nr, nc, new_k))
        return -1