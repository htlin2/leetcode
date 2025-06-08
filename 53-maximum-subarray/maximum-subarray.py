class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left, right):
            if left > right: return float('-inf')
            mid = (left + right) // 2
            curr_sum = left_sum = 0
            for i in range(mid - 1, left - 1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)
            curr_sum = right_sum = 0
            for i in range(mid + 1, right + 1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
            combined = left_sum + right_sum + nums[mid]
            sub_left = helper(left, mid - 1)
            sub_right = helper(mid + 1, right)
            return max(combined, sub_left, sub_right)
        return helper(0, len(nums) - 1)
