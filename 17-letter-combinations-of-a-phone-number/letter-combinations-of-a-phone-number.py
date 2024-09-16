class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': '',
        }
        if not digits: return ''
        res = []
        N = len(digits)
        def backtrack(i, combos):
            if i == N:
                res.append(''.join(combos))
                return
            for char in digit_map[digits[i]]:
                combos.append(char)
                backtrack(i + 1, combos)
                combos.pop()
        backtrack(0, [])
        return res

"""

"""