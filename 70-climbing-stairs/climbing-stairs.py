class Solution:
    def climbStairs(self, n: int) -> int:
        dp = collections.defaultdict(int)
        ans = 0
        def dfs(n):
            nonlocal ans
            if n <= 2: return n
            if n in dp: return dp[n]
            ans += dfs(n - 1) + dfs(n - 2)
            dp[n] = ans
            return ans
        return dfs(n)
"""
n = 2
0 1 2
1 1 2   

n = 3
-1  0  1  2  3
 0  1  1  2  3
 p  p  p  c

"""