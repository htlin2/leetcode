class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        window_size = sum(nums)
        window = 0
        max_ones = 0
        left = 0
        for right in range(N):
            window += nums[right]
            if right - left + 1 > window_size:
                window -= nums[left]
                left += 1
            max_ones = max(max_ones, window)
        return window_size - max_ones