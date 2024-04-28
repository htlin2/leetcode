class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(rem, i):
            if rem == 0: return 1
            if rem < 0 or i == len(coins): return 0
            if (rem ,i) in memo: return memo[rem, i]
            res = dfs(rem - coins[i], i) + dfs(rem, i + 1)
            memo[rem, i] = res
            return res
        return dfs(amount, 0)