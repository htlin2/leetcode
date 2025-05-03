class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1
        def pow(x, n):
            res = 1
            while n:
                if n % 2 == 1:
                    res = (res * x) % MOD
                    n -= 1
                else:
                    x = (x * x) % MOD
                    n = n // 2
            return res
        odd = n // 2 + n % 2
        even = n // 2
        return (pow(5, odd) * pow(4, even)) % MOD
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