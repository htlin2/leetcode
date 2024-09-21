class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = collections.defaultdict(int) # i: total
        for i in range(N):
            rob = dp[i - 2] + nums[i]
            skip = dp[i - 1]
            dp[i] = max(rob, skip)
        return dp[N - 1]

"""
dp

"""