class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums = nums + [0]
        stack = []
        for r in range(len(nums)):
            next_small = nums[r]
            while stack and nums[stack[-1]] >= next_small:
                prev_small_idx = stack.pop()
                k = r - stack[-1] - 1 if stack else r
                if nums[prev_small_idx] > threshold / k:
                    return k
            stack.append(r)
        return -1

"""
monotonic stack increasing
previous small, next small
Input: nums = [1,3,4,3,1], threshold = 6
idx            0,1,2,3,4
Output: 3
stack = 1,3
next_small = 3
prev_small = 3
k = 2
"""