class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        left, right = grid[0][0], grid[-1][-1]
        def get_count(mid):
            count = 0
            for row in grid:
                count += bisect.bisect_right(row, mid)
            return count
        while left <= right:
            mid = (left + right) // 2
            count = get_count(mid)
            if count == k:
                right = mid - 1
            elif count <= k:
                left = mid + 1
            else:
                right = mid - 1
        return left