class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(l, r):
            if l > r: return float('-inf')
            left_sum = right_sum = total_sum = 0
            mid = (l + r) // 2
            curr_sum = 0
            for i in range(mid - 1, l - 1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)
            curr_sum = 0
            for i in range(mid + 1, r + 1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
            combined_sum = left_sum + nums[mid] + right_sum
            left_max = helper(l, mid - 1)
            right_max = helper(mid + 1, r)
            return max(left_max, right_max, combined_sum)
        return helper(0, len(nums) - 1)