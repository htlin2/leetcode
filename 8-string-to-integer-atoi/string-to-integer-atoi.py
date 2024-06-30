class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        i = 0
        is_positive = True
        if s[i] == '-':
            is_positive = False
            i += 1
        elif s[i] == '+':
            is_positive = True
            i += 1
        ans = 0
        while i < len(s) and s[i].isdigit():
            ans *= 10
            ans += int(s[i])
            i += 1
        if not is_positive:
            ans *= -1
        if -2 ** 31 <= ans <= 2 ** 31 -1:
            return ans
        elif ans < -2 ** 31:
            return -2 ** 31
        else:
            return 2 ** 31 - 1