import bisect

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n == target:
                res.append(i)
        return res
"""
Brute Force + sort
loop from beginning to find left idx
loop from end to find right idx
Time: O(n log n)
Space: O(n)
"""