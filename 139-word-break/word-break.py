class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(s):
            if not s: return True
            if s in memo: return memo[s]
            res = False
            for w in wordDict:
                if not s.startswith(w): continue
                substr = s[len(w):]
                res = res or dfs(substr)
            memo[s] = res
            return res
        return dfs(s)
        
"""
backtracking
s = "applepenapple", wordDict = ["appl","pen", "apple"]

"applepenapple"
 
"""