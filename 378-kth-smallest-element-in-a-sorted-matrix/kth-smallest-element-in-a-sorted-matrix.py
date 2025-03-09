class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        nums = []
        for row in grid:
            nums = [*nums, *row]
        nums.sort()
        return nums[k - 1]
"""
brute force
"""