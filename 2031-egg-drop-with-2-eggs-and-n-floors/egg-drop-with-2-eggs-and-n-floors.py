class Solution:
    def twoEggDrop(self, n: int) -> int:
        # Initialize a DP table with (n+1) entries, since floors are 0-indexed
        dp = [0] * (n + 1)
        
        # The worst-case attempts can be at most the number of floors
        for m in range(1, n + 1):
            dp[m] = m

        # We iterate through the number of floors
        for m in range(1, n + 1):
            for f in range(1, m + 1):
                dp[m] = min(dp[m], 1 + max(f - 1, dp[m - f]))
        
        return dp[n]