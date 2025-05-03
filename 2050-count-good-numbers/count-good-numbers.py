class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1
        def pow(base, n):
            if n == 0:
                return 1
            half = pow(base * base % MOD, n // 2) % MOD
            if n % 2 == 1:
                half *= base
            return half % MOD
        odd = 1 if n % 2 else 0
        return (pow(5, n // 2 + odd) * pow(4, n // 2)) % MOD
"""
n = 1
5

n = 2
5 * 4 = 20

n = 3
5 * 4 * 5 = 100

n = 4
5 * 4 * 5 * 4 = 400
"""