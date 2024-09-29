class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        open_p = 0
        for char in s:
            if char == '(':
                open_p += 1
            elif char == ')':
                if open_p >= 1:
                    open_p -= 1
                else:
                    res += 1
        return res + open_p