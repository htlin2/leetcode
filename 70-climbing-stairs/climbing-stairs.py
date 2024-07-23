class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 0, 1
        for i in range(n):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr

"""
1. recurrsion + memo
    memo = {}
    def dfs(n):
        if n <= 2: return n
        if n in memo: return memo[n]
        res = dfs(n - 1) + dfs(n - 2)
        memo[n] = res
        return res
    time: O(n)
    space: O(n)
2. tabulation
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]
    time: O(n)
    space: O(n)
3. greedy
    prev, curr = 1, 1
    for i in range(n):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr
"""