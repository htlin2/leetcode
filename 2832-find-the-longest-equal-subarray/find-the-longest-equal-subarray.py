import collections
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        window = collections.defaultdict(int)
        max_f = 0
        left = 0
        for right, num in enumerate(nums):
            window[num] += 1
            max_f = max(max_f, window[num])
            while (right - left + 1 - max_f) > k:
                window[nums[left]] -= 1
                left += 1
        return max_f
            

"""
sliding window variable
Input: nums = [1,3,2,3,1,3], k = 3
counter = {1: 1`, 3: 3, 2: 1}
max_f = 3
[1,3,2,3,1,3,5,6]
   l         i
"""