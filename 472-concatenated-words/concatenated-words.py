class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        res = []
        memo = {}
        def dfs(w):
            if w in memo:
                return memo[w]
            for i in range(1, len(w)):
                prefix = w[:i]
                postfix = w[i:]
                if prefix in words_set:
                    if postfix in words_set or dfs(postfix):
                        memo[w] = True
                        return True
            memo[w] = False
            return False

        for w in words:
            if dfs(w):
                res.append(w)
        return res