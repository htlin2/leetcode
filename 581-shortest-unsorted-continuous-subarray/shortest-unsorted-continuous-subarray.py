class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        N = len(nums)
        left, right = 0, N - 1
        while left <= right and left < N and nums[left] == sorted_nums[left]:
            left += 1
        while left <= right and right >= 0 and nums[right] == sorted_nums[right]:
            right -= 1
        if left >= right: return 0
        return right - left + 1

"""

"""