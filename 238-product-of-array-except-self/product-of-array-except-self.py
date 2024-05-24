class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_sums = [1] * N
        prefix = 1
        for i in range(N):
            prefix_sums[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(N - 1, -1, -1):
            prefix_sums[i] *= postfix
            postfix *= nums[i]
        return prefix_sums
        

"""
1. brute force
2 for loops
Time: O(n^2)
space: O(1)

2. prefix_sums
nums = [ 1, 2, 3, 4]
prefix [ 1, 1, 2, 6]
postfix[24,12, 4, 1]
ans    [24,12, 8, 6]
time: O(n)
space: O(n)
"""