class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def pow(x, n):
            base = 1
            while n:
                if n % 2 == 1:
                    base *= x
                    base = base % MOD
                    n -= 1
                else:
                    x *= x
                    x = x % MOD
                    n = n // 2
            return base
        odd = n // 2 + (1 if n % 2 == 1 else 0)
        even = n // 2
        return pow(5, odd) % MOD * pow(4, even) % MOD
"""
n = 1
5

n = 2
5 * 4 = 20?

n = 3
5 ^ 2 * 4 = 100

n = 4
5^2 * 4^2 = 20^2 = 400
"""