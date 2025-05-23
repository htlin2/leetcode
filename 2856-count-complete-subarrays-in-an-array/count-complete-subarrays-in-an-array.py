class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq_length = len(set(nums))
        window = collections.defaultdict(int)
        res = 0
        left = 0
        for right in range(len(nums)):
            window[nums[right]] += 1
            while len(window) == uniq_length:
                res += len(nums) - right
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
        return res
"""
sliding window
Input: nums = [1,3,1,2,2]
Output: 4
uniq_length = 3
1,3,1,2 -> N (5) - 3 = 2
312 -> N - 4 + 1 = 2

Input: nums = [5,5,5,5]
output: 10
uniq_length = 1
5 -> 4 - 1 + 1 = 4
 5 -> 4 - 2 + 1 = 3
   5 -> 4 - 3 + 1 = 2
     5 -> 4 - 4 + 1 = 1
"""