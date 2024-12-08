class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            peak = nums[mid]
            peak_left = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            peak_right = nums[mid + 1] if mid + 1 < N else float('-inf')
            is_peak = peak_left <= peak and peak_right <= peak
            if is_peak: return mid
            if peak_left <= peak <= peak_right:
                left = mid + 1
            else:
                right = mid - 1
        return right

"""
binary search

"""