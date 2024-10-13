class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        curr_ones = 0
        res, left = total_ones, 0
        for right, num in enumerate(nums):
            curr_ones += num
            if right - left + 1 > total_ones:
                curr_ones -= nums[left]
                left += 1
            res = min(res, total_ones - curr_ones)
        return res
"""
sliding window
Input: data = [1,0,1,0,1]
output: 1
res = 2
total_ones = 3
curr_ones = 1
 1, 0, 1, 0, 1]
l      r      

"""