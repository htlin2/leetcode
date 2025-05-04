class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = set()
        for i in range(1, n + 1):
            if i in factors:
                continue
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        res = sorted(list(factors))
        return res[k - 1] if k - 1 < len(res) else -1