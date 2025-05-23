class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            prev_num = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            next_num = nums[mid + 1] if mid + 1 < len(nums) else float('inf')
            if nums[mid] != prev_num and nums[mid] != next_num:
                return nums[mid]
            left_size = mid
            if nums[mid] == next_num:
                left_size += 1
            if left_size % 2 == 1:
                left = mid + 1
            else:
                right = mid - 1
        return nums[right]
"""
binary search
"""