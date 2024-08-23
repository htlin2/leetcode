class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr_sum = float('-inf')
        for n in nums:
            curr_sum = max(curr_sum + n, n)
            res = max(curr_sum, res)
        return res


"""
prefix sum
sliding window x b/c it has negative
[-2, 1,-3,4,-1, 2, 1,-5, 4
greedy
        -2, 1 -2,4,-3, 5, 6,
        -2, 1,-1,4, 1, 6         max(curr_sum, curr)
res     -2, 1, 1,4, 4, 6
res = 0
 -2,-1,-4,0,-1,-1, 0,-5,-1 = prefix_sum
 -2,
"""