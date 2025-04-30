class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] >= num:
                prev_small_idx = stack.pop()
                k = i - stack[-1] - 1 if stack else i
                if nums[prev_small_idx] > threshold / k:
                    return k
            stack.append(i)
        return -1
"""
monotonic stack increasing

"""