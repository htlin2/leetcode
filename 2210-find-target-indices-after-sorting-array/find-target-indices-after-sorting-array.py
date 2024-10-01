class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count_less = 0
        count_target = 0
        for n in nums:
            if n == target:
                count_target += 1
            elif n < target:
                count_less += 1
        return [i + count_less for i in range(count_target)]
"""
Optimized Counting
Time: O(n)
Space: O(1) if ignore space for output
"""