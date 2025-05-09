class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        min_heap = [] # (val, row, col)
        for c in range(len(grid[0])):
            heapq.heappush(min_heap, (grid[0][c], 0, c))
        while k:
            k -= 1
            val, row, col = heapq.heappop(min_heap)
            if row + 1 < len(grid):
                heapq.heappush(min_heap, (grid[row + 1][col], row + 1, col))
        return val
"""
k = 8
Input: matrix = [
    [ 1, 5, 9],
    [10,11,13],
    [12,13,15]
], 

min_heap = , , 13
k = 1
"""