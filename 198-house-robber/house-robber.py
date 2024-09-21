class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {} # i: total
        def dfs(i):
            if i >= N: return 0
            if i in memo: return memo[i]
            # rob
            res = dfs(i + 2) + nums[i]
            # skip
            res = max(res, dfs(i + 1))
            memo[i] = res
            return res
        return dfs(0)

"""
dp

"""