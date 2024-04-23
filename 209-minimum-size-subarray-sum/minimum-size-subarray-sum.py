class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2) prefix sum + binary search weight left
            # time: O(n log n)
            # space: O(n)
        N = len(nums)
        prefix_sums = []
        curr_sum = 0
        min_window_length = float('inf')
        for i in range(N):
            curr_sum += nums[i]
            if curr_sum >= target:
                min_window_length = min(min_window_length, i + 1)
            prefix_sums.append(curr_sum)

        for i in range(N):
            to_find = prefix_sums[i] + target
            idx = bisect.bisect_left(prefix_sums, to_find)
            if idx == N: continue
            min_window_length = min(min_window_length, idx - i)
        return 0 if min_window_length == float('inf') else min_window_length