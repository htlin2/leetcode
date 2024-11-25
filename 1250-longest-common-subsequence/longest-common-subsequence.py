class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {} # (i, j): lcs
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in memo: return memo[i, j]
            res = 0
            if text1[i] == text2[j]:
                res = dfs(i + 1, j + 1) + 1
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))
            memo[i, j] = res
            return res
        return dfs(0, 0)

"""
Input: text1 = "abcde", text2 = "ace" 

output: ace
mono stack? 
stack = ace
max_sub = 1

Input: text1 = "xabcde", text2 = "acfe" 
                012345
output: ace
stack = 1

dp
skip text1 or skip text2
find longest
"""