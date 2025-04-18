class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        min_heap = [] # (num, row, col)
        for col in range(len(grid[0])):
            num = grid[0][col]
            heapq.heappush(min_heap, (num, 0, col))
        while k > 1:
            k -= 1
            num, row, col = heapq.heappop(min_heap)
            if row + 1 < len(grid):
                next_num = grid[row + 1][col]
                heapq.heappush(min_heap, (next_num, row + 1, col))
        return min_heap[0][0]

"""
1. heap + linked list
O(n log n + k)

2. binary search
range = m
O(n log m)
"""