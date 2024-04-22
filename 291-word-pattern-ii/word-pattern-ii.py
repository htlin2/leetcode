class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        h1, h2 = {}, {}
        def dfs(i, j):
            if i == len(p) and j == len(s): return True
            if i == len(p) or j == len(s): return False
            if p[i] in h1:
                substr = h1[p[i]]
                if s.find(substr, j) != j: return False
                return dfs(i + 1, j + len(substr))
            for k in range(j, len(s)):
                substr = s[j:k + 1]
                if substr in h2: continue
                h1[p[i]] = substr
                h2[substr] = p[i]
                if dfs(i + 1, j + len(substr)): return True
                del h1[p[i]]
                del h2[substr]
            return False
        return dfs(0, 0)
