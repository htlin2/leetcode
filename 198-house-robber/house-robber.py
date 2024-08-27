class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}
        def dfs(i):
            if i >= N: return 0
            if i in memo: return memo[i]
            # skip
            res = dfs(i + 1)
            # rob
            res = max(res, dfs(i + 2) + nums[i])
            memo[i] = res
            return res
        return dfs(0)
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