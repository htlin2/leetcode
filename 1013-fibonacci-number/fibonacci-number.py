class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n < 2:
                return n
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]
        return dfs(n)

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