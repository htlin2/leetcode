class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        min_heap = [] #(v, r, c)
        for c in range(len(grid[0])):
            heapq.heappush(min_heap, (grid[0][c], 0, c))
        while k - 1:
            k -= 1
            _, r, c = heapq.heappop(min_heap)
            if r + 1 < len(grid[0]):
                heapq.heappush(min_heap, (grid[r + 1][c], r + 1, c))
        return min_heap[0][0]
"""
k = 8
Input: matrix = [
    [ 1, 5, 9],
    [10,11,13],
    [12,13,15],
]
1. binary search + bisect weight right
left = 1, right = 15
Time: O(n log n + log m)
Space:

2. binary search + for loop
O(n log n + log m)
"""