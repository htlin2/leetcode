class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = collections.defaultdict(int)        
        dp[N - 1] = nums[N - 1]
        for i in range(N - 1, -1, -1):
            skip = dp[i + 1]
            rob = dp[i + 2] + nums[i]
            dp[i] = max(skip, rob)
        return dp[0]
"""
input = [2,6,2,1,0], output = 7
         - r - r
2 choices > rob or skip
if rob, we have to skip

1: dfs + memo
memo = {} # idx: max_money
dfs(curr_index):
    # skip
    dfs(curr_index + 1)
    # rob
    dfs(curr_index + 2) + money
    max (skip, rob)

2: tabulation
iterate thought nums from back to front
    check dp[curr_index] = max(dp[curr_index - 1], dp[curr_index - 2])
"""