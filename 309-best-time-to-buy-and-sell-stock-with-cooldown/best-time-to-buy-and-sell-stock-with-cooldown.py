class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        memo = {} # (i, is_buying): max_profit
        def dfs(i, is_buying):
            # base case: if i reaches end of N: return 0
            if i >= N: return 0
            # if params in memo: return memo[params]
            if (i, is_buying) in memo: return memo[i, is_buying]
            if is_buying:
                # next level dfs - prices[i] or cooldown
                res = max(dfs(i + 1, False) - prices[i], dfs(i + 1, is_buying))
            else:
                # sell or cooldown
                res = max(dfs(i + 2, True) + prices[i], dfs(i + 1, is_buying))
            memo[i, is_buying] = res
            return res
        return dfs(0, True)