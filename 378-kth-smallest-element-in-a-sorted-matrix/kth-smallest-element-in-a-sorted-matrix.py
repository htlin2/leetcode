class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        left, right = grid[0][0], grid[-1][-1]
        def get_k(mid):
            maybe_k = 0
            for row in grid:
                maybe_k += bisect.bisect_right(row, mid)
            return maybe_k

        while left <= right:
            mid = (left + right) // 2
            maybe_k = get_k(mid)
            if maybe_k < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
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