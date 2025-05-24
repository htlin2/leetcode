class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            prev_num = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            next_num = nums[mid + 1] if mid + 1 < len(nums) else float('inf')
            if nums[mid] != prev_num and nums[mid] != next_num:
                return nums[mid]
            left_size = mid - 1 if prev_num == nums[mid] else mid
            if left_size % 2 == 1:
                # odd
                right = mid - 1
            else:
                # even
                left = mid + 1
        return nums[right]