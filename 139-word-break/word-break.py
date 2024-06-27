class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        memo = {} # index: bool
        def dfs(i):
            if i == N: return True
            if i in memo: return memo[i]
            res = False
            for w in wordDict:
                if s[i:i+len(w)] != w: continue
                res = (res or dfs(i + len(w)))
            memo[i] = res
            return res
        return dfs(0)
        
"""
backtracking
s = "applepenapple", wordDict = ["appl","pen", "apple"]

"applepenapple"
 
"""