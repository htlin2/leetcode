class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        min_heap = [] # (value, row, col)
        for col in range(len(grid[0])):
            to_add = (grid[0][col], 0, col)
            heapq.heappush(min_heap, to_add)
        while k > 1:
            v, r, c = heapq.heappop(min_heap)
            if r + 1 < len(grid):
                to_add = (grid[r + 1][c], r + 1, c)
                heapq.heappush(min_heap, to_add)
            k -= 1
        return min_heap[0][0]
