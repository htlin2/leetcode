class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def pow(x, n):
            res = 1
            while n:
                is_odd = n % 2 == 1
                if is_odd:
                    res = res * x % MOD
                    n -= 1
                else:
                    x = x * x % MOD
                    n = n // 2
            return res % MOD
        odd = n % 2 + n // 2
        even = n // 2
        return (pow(5, odd) * pow(4, even)) % MOD