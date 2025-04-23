class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            prev_num = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            next_num = nums[mid + 1] if mid + 1 < N else float('inf')
            num = nums[mid]
            if prev_num != num and num != next_num:
                return num
            left_arr = mid - 1 if prev_num == num else mid
            if left_arr % 2 == 0:
                # even
                left = mid + 1
            else:
                # odd
                right = mid - 1
