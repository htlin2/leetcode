class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        N = len(weights)
        nums = []
        for i in range(N - 1):
            num = weights[i] + weights[i + 1]
            nums.append(num)
        nums.sort()
        i = k - 1
        high = sum(nums[-i:])
        low = sum(nums[:i])
        return high - low