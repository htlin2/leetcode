class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        is_negative = True if n < 0 else False
        n = abs(n)
        extra = 1
        while n > 1:
            if n % 2:
                extra *= x
            x *= x
            n = n // 2
        x *= extra
        return 1/x if is_negative else x
"""
2^10
4^5
16^2 * 4

"""