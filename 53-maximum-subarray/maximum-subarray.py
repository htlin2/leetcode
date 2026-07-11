class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        N = len(nums)
        l = 0
        curr_sum, max_sum = 0, nums[0]
        for r in range(N):
            num = nums[r]
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                l = r
                curr_sum = 0
        return max_sum
"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

two pointers
 [-2, 1,-3, 4,-1, 2, 1,-5, 4]
l  0, 1,-3, 4
r -2, 1,-3, 4, 3, 2, 1, r
s  0, 1,-2, 4, 3, 5, 6, 1
m     1     4     5, 6

if curr_sum < 0, move left pointer

"""