class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [] # val, r, c
        for c in range(COLS):
            val = grid[0][c]
            to_add = (val, 0, c)
            heapq.heappush(min_heap, to_add)
        k -= 1
        while k:
            k -= 1
            _, r, c = heapq.heappop(min_heap)
            if r + 1 < ROWS:
                heapq.heappush(min_heap,(grid[r + 1][c], r + 1, c))
        return min_heap[0][0]