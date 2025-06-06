class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            curr_num = nums[mid]
            prev_num = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            next_num = nums[mid + 1] if mid + 1 < len(nums) else float('inf')
            if curr_num != prev_num and curr_num != next_num:
                return curr_num
            left_size = mid + 1 if curr_num == next_num else mid
            left_size += 1
            if left_size % 2 == 1:
                # odd
                right = mid - 1
            else:
                left = mid + 1
        return nums[right]