class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = collections.defaultdict(int)
        for i in range(len(nums) - 1, -1, -1):
            # skip
            skip = dp[i + 1]
            # rob
            rob = dp[i + 2] + nums[i]
            dp[i] = max(skip, rob)
        return dp[0]