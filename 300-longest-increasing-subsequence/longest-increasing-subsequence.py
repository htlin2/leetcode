class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = collections.defaultdict(lambda: 1)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        res = 1
        for v in dp.values():
            res = max(res, v)
        return res
"""
monotonic stack increasing + sliding window condition
dfs

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
[2,3,7,101,18]

Input: nums = [0,1,0,3,2,3]
Output: 4
[0,2,3]
[0,1,2,3]
[0,1,2,3]

Input: nums = [7,7,7,7,7,7,7]
Output: 1
[7]

nums = [1,3,6,7,9,4,10,5,6]
output = 6
[1,3,6,7,9,10]
"""