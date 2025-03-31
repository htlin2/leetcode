class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        left, right = grid[0][0], grid[-1][-1]
        def less_than_mid_counts(mid):
            count = 0
            r, c = len(grid) - 1, 0
            while r >= 0 and c < len(grid[0]):
                if grid[r][c] <= mid:
                    count += r + 1
                    c += 1
                else:
                    r -= 1
            return count

        while left <= right:
            mid = (left + right) // 2
            if less_than_mid_counts(mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left