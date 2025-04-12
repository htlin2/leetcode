class Solution:
    def reverse(self, x: int) -> int:
        MAX_RANGE = 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        res = 0
        x = abs(x)
        while x:
            digit = x % 10
            res = res * 10 + digit
            if res > MAX_RANGE:
                return 0
            x = x // 10
        return res * sign