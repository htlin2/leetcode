class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        nums = []
        for i in range(1, len(weights)):
            curr_sum = weights[i] + weights[i - 1]
            nums.append(curr_sum)
        nums.sort()
        k -= 1
        if not k: return 0
        min_arr = nums[:k]
        max_arr = nums[-(k):]
        return sum(max_arr) - sum(min_arr)
"""
Input: weights = [1,3,5,1], k = 2
Output: 4

4,8,6

"""