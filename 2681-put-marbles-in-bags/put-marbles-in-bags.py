class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        N = len(weights)
        nums = []
        for i in range(N - 1):
            nums.append(weights[i] + weights[i + 1])
        nums.sort()
        i = k - 1
        max_score = sum(nums[-i:])
        min_score = sum(nums[:i])
        return max_score - min_score