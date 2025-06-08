class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo: return memo[i]
            if i >= len(nums): return 0
            # skip
            res = dfs(i + 1)
            # rob
            res = max(res, dfs(i + 2) + nums[i])
            memo[i] = res
            return res
        return dfs(0)