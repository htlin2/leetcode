class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_positive = n >= 0
        n = abs(n)
        ans = 1
        while n:
            if n % 2 == 1:
                n -= 1
                ans *= x
            n = n // 2
            x = x * x
        return ans if is_positive else 1 / ans