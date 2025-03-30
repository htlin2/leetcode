class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        left, right = grid[0][0], grid[-1][-1]
        def less_than_mid_counts(mid):
            count = 0
            for row in grid:
                count += bisect.bisect_right(row, mid)
            return count

        while left <= right:
            mid = (left + right) // 2
            if less_than_mid_counts(mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
"""
heap + queue
k = 8
Input: grid = 
[
    [1,5,9],
    [10,11,13],
    [12,13,15]
]
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
k = 4
[ 1, 5, 9]
[10,11,13]
[12,]
"""