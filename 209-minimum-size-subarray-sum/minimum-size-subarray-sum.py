class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 1) sliding window variable
            # left + right pointers and keep track window sum == target
            # time: O(n)
            # space: O(1)
        N = len(nums)
        left = 0
        window_sum = 0
        min_window_length = float('inf')
        for right in range(N):
            window_sum += nums[right]
            while window_sum >= target and left <= right:
                min_window_length = min(min_window_length, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return min_window_length if min_window_length != float('inf') else 0
        # 2) prefix sum + binary search weight left
            # time: O(n log n)
            # space: O(n)
        # 3) prefix sum + hashmap
            # time: O(n)
            # space: O(n)