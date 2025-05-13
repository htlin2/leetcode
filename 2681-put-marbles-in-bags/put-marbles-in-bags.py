class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        nums = []
        for i in range(1, len(weights)):
            curr_sum = weights[i] + weights[i - 1]
            nums.append(curr_sum)
        nums.sort()
        i = k - 1
        max_score = sum(nums[-i:])
        min_score = sum(nums[:i])
        return max_score - min_score
"""
Input: weights = [1,3,5,1], k = 2
4,8,6
"""