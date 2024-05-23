class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = collections.defaultdict(lambda: float('inf'))
        dp[0] = 0
        for c in coins:
            for a in range(1, amount + 1):
                dp[a] = min(dp[a - c] + 1, dp[a])
        return dp[amount] if dp[amount] != float('inf') else -1
"""
1. dfs + memo
Input: coins = [1,2,5], amount = 6
Time: O(2^n)
Space: O(1)

memo:
Time: O(n)
Space: O(n)

2. tabulation

"""