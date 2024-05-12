class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = float('-inf'), float('-inf')
        # iterate through nums:
        for n in nums:
            # keep track of curr_sum = max(nums[i], curr_sum + nums[i])
            curr_sum = max(n, curr_sum + n)
            # keep track of max_sum
            max_sum = max(max_sum, curr_sum)
        return max_sum
"""
1. brute force
two for loops to find largest sum
Time: O(n^2)
Space: O(1)

2. greedy
nums = [-2, 1,-3,4,-1,2,1,-5,4]
curr_s  -2, 1,-2,4
max_sum -2, 1, 1,4
curr_sum = max(nums[i], curr_sum + nums[i])
Time: O(n)
Space: O(1)

"""