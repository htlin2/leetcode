class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1
        for i in range(len(coins)):
            for a in range(amount + 1):
                delta = a - coins[i]
                if delta < 0: continue
                dp[a] += dp[delta]
        return dp[amount]