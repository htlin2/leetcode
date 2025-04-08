class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        left, right = grid[0][0], grid[-1][-1]
        def get_k(mid):
            counts = 0
            row, col = len(grid) - 1, 0
            while row >= 0 and col < len(grid[0]):
                if grid[row][col] <= mid:
                    counts += row + 1
                    col += 1
                else:
                    row -= 1
            return counts

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