class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        adj = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if not digits: return []
        N = len(digits)
        res = []
        def dfs(temp, i):
            if len(temp) == N:
                res.append(temp[:])
                return
            for char in adj[digits[i]]:
                dfs(temp + char, i + 1)
        dfs('', 0)
        return res

"""
backtracking

"""