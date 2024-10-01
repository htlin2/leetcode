import bisect

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        nums.sort()
        left_idx = bisect.bisect_left(nums, target)
        if not (0 <= left_idx < N):
            return []
        right_idx = bisect.bisect_right(nums, target)
        return [i for i in range(left_idx, right_idx)]
"""
Binary Search
weight left to find left idx
weight right to find right idx
slice to create the result list
Time: O(n log n)
Space: O(n)

Brute Force
loop from beginning to find left idx
loop from end to find right idx
Time: O(n log n)
Space: O(n)
"""