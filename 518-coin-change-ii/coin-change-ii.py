class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} # (rem, i): count
        def dfs(rem, i):
            if rem == 0: return 1
            if rem < 0 or i == len(coins): return 0
            if (rem, i) in memo: return memo[rem, i]
            res = 0
            for j in range(i, len(coins)):
                res += dfs(rem - coins[j], j)
            memo[rem, i] = res
            return res
        return dfs(amount, 0)