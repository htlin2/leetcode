class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        is_negative = True if n < 0 else False
        n = abs(n)
        curr = self.myPow(x * x, n // 2)
        if n % 2:
            curr *= x
        return 1/curr if is_negative else curr
"""
2^10
4^5
16^2 * 4

"""