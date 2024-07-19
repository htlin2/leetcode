class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # tabulation
        ROWS, COLS = m, n
        dp = collections.defaultdict(int)
        dp[0, -1] = 1
        for r in range(ROWS):
            for c in range(COLS):
                dp[r, c] = dp[r - 1, c] + dp[r, c - 1]
        return dp[ROWS - 1, COLS - 1]
"""
backtracking + memo
dfs(r, c):
    if r == end and c == end: return 1
    if r, c in memo: return memo result
    iterate through right or down
        check for out of bound
time: O(n * m)
space: O(n * m)


tabulation
111
123
time: O(n * m)
space: O(n * m)
"""