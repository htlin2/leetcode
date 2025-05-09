class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        def get_total(mid):
            res = 0
            for row in grid:
                res += bisect.bisect_right(row, mid)
            return res
        left, right = grid[0][0], grid[-1][-1]
        while left <= right:
            mid = (left + right) // 2
            total = get_total(mid)
            if total == k:
                right = mid - 1
            elif total < k:
                left = mid + 1
            else:
                right = mid - 1
        return left