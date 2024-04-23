class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h = {}
        prefix_sum = 0
        max_length = 0
        for i, n in enumerate(nums):
            if n == 0:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            if prefix_sum == 0:
                max_length = max(i + 1, max_length)
            if prefix_sum in h:
                max_length = max(i - h[prefix_sum], max_length)
            if prefix_sum not in h:
                h[prefix_sum] = i
        if prefix_sum == 0:
            return len(nums)
        return max_length