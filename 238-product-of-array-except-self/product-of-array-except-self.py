class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_sums = []
        prefix = 1
        for i in range(N):
            prefix_sums.append(prefix)
            prefix *= nums[i]
        postfix_sums = [0] * N
        postfix = 1
        for i in range(N - 1, -1, -1):
            postfix_sums[i] = postfix
            postfix *= nums[i]
        ans = [0] * N
        for i in range(N):
            ans[i] = prefix_sums[i] * postfix_sums[i]
        return ans
        

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