class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [0] * (N + 2)
        for i in range(N - 1, -1, -1):
            buy_sell = 0
            for j in range(i + 1, N):
                buy_sell = max(buy_sell, dp[j + 2] + prices[j] - prices[i])
            skip = dp[i + 1]
            dp[i] = max(buy_sell, skip)
        return dp[0]