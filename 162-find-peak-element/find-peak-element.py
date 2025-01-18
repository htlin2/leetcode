class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            left_num = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            right_num = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')
            if left_num <= nums[mid] and right_num <= nums[mid]:
                return mid
            if left_num <= right_num:
                left = mid + 1
            else:
                right = mid - 1
        return 0