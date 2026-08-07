class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        memo = {}
        def dfs(i, curr):
            if i >= N or curr > amount: return float('inf')
            if curr == amount: return 0
            if (i, curr) in memo: return memo[(i, curr)]
            # take
            take = dfs(i, curr + coins[i]) + 1
            # skip
            skip = dfs(i + 1, curr)
            memo[(i, curr)] = min(take, skip)
            return memo[(i, curr)]
        res = dfs(0, 0)
        return res if res != float('inf') else -1
"""
backtracking

"""