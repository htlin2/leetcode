class Solution:
    def romanToInt(self, s: str) -> int:
        h = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        res = 0
        N = len(s)

        for i in range(N):
            char = s[i]
            res += h[char]
            if i - 1 >= 0:
                prev_char = s[i - 1] + s[i]
                if prev_char in h:
                    res += h[prev_char]
                    res -= h[char]
                    res -= h[s[i - 1]]
        return res