class Solution:
    def myAtoi(self, s: str) -> int:
        # strip out leading spaces (can also use s = s.lstrip())
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s): return 0

        # check leading sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # add int to ans
        ans = 0
        while i < len(s) and s[i].isdigit():
            ans *= 10
            ans += int(s[i])
            i += 1
        ans *= sign

        # check out of bound
        if ans < -2 ** 31:
            return -2 ** 31
        elif 2 ** 31 - 1 < ans:
            return 2 ** 31 - 1
        return ans