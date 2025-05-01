class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            curr_num = nums[mid]
            prev_num = nums[mid - 1] if mid - 1 >= 0 else nums[-1]
            left_length = mid - 1 if prev_num == curr_num else mid
            if left_length % 2 == 1:
                right = mid - 1
            else:
                left = mid + 1
        return nums[right]