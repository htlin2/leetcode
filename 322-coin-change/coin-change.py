class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} # (i, rem): min_coins_count
        def dfs(i, rem):
            # base case: if rem == 0: return count
            if rem == 0: return 0
            if rem < 0 or i == len(coins): return float('inf')
            if (i, rem) in memo: return memo[i, rem]
            # add coin
            res = dfs(i, rem - coins[i]) + 1
            # skip coin
            res = min(res, dfs(i + 1, rem))
            # add to memo
            memo[i, rem] = res
            return res
        ans = dfs(0, amount)
        return ans if ans != float('inf') else -1
"""
dfs + memo
Input: coins = [1,2,5], amount = 6
Time: O(2^n)
Space: O(1)

memo:
Time: O(n)
Space: O(n)
"""