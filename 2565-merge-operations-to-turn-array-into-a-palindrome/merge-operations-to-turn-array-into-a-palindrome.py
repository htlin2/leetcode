class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        left, right = -1, len(nums)
        left_sum = right_sum = 0
        while left < right:
            if left_sum == right_sum:
                left += 1
                right -= 1
                left_sum += nums[left]
                right_sum += nums[right]
                continue
            res += 1
            if left_sum > right_sum:
                right -= 1
                right_sum += nums[right]
            else:
                left += 1
                left_sum += nums[left]
        return res
"""
dp - dfs + memo
two pointers
Input: nums = [4,3,2,1,2,3,1]
Output: 2
1) [4,3,2,3,3,1]
2) [4,3,2,3,4]

Input: nums = [1,2,3,4]
Output: 3
1) [3,3,4]
2) [6,4]
3) [10]

"""