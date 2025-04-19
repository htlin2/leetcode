class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            prev_num = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            next_num = nums[mid + 1] if mid + 1 < N else float('inf')
            mid_num = nums[mid]
            if prev_num != mid_num and mid_num != next_num:
                return mid_num
            left_size = mid - 1 if prev_num == mid_num else mid
            if left_size % 2:
                # odd left
                right = mid - 1
            else:
                # even left
                left = mid + 1
        return nums[left]