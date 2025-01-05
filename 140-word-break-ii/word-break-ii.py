class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        res = []
        def dfs(s, temp):
            if not s:
                res.append(' '.join(temp))
            for word in words:
                substr = s[0:len(word)]
                if word in s and s.index(word) == 0:
                    substr = s[len(word):]
                    dfs(substr, temp + [word])
        dfs(s, [])
        return res
"""
Trie? DFS++

"""