class Solution:
    def fib(self, n: int) -> int:
        dp = collections.defaultdict(int)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
"""
1. recurrsion
    dfs
    base case: if n < 2: return n
    return n - 1 + n -2
    time: O(2 ^ n)
    space: O(n) 
2. recurrsion + memo
    save {n: result}
    add memo after base
    time: O(n)
    space: O(n)
3. dp - tabulation
    dp = []
    time: O(n)
    space: O(n)
4. while loop
    track prev, curr values
    time:O(n)
    space:O(1)
"""