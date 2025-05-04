class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = set()
        for i in range(1, n + 1):
            if i in factors:
                continue
            if n % i == 0:
                factors.add(i)
                k -= 1
                if k == 0:
                    return i
        return -1