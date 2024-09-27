class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        N = len(digits)
        res = []
        def dfs(i, temp):
            if i == N:
                substr = ''.join(temp)
                res.append(substr)
                return
            for char in hashmap[digits[i]]:
                temp.append(char)
                dfs(i + 1, temp)
                temp.pop()
        dfs(0, [])
        return res
