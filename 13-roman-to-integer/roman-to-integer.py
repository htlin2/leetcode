class Solution:
    def romanToInt(self, s: str) -> int:
        h = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        for i, char in enumerate(s):
            if i + 1 < len(s) and h[char] < h[s[i + 1]]:
                res -= h[char]
            else:
                res += h[char]
        return res