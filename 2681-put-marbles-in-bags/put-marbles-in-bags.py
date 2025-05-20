class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        nums = []
        for i in range(1, len(weights)):
            nums.append(weights[i] + weights[i - 1])
        nums.sort()
        i = k - 1
        max_arr = nums[-i:]
        min_arr = nums[:i]
        return sum(max_arr) - sum(min_arr)