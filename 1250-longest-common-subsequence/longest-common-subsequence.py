class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # case 1 DFS + memo
        # text1 = i, text2 = j
        memo = {} # (i, j): max_length
        def dfs(i, j):
            # base case: if i or j reaches end return 0
            if i >= len(text1) or j >= len(text2): return 0
            if (i, j) in memo: return memo[i, j]
            if text1[i] == text2[j]:
                res = dfs(i + 1, j + 1) + 1
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))
            memo[i, j] = res
            return res
        return dfs(0, 0)
        # time: O(n + m)
        # space: O(n + m)

        # case 2 tabulation
        # dp = [0] * len(text1)
        # iterate r through text2
            # iterate c through text1
                # if text1[c] == text2[r]:
                    # dp[c] = prev_dp[c - 1] + 1
                # else:
                    # dp[c] = max(prev_dp[c], dp[c - 1])
            # prev_dp = dp
        # return dp[-1]
        