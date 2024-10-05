class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        N = len(nums)
        stack = [] # monotonic stack increasing
        for i in range(N):
            next_smaller = nums[i]
            while stack and nums[stack[-1]] > next_smaller:
                highest_idx = stack.pop()
                k = i - stack[-1] - 1 if stack else i
                if nums[highest_idx] > threshold / k:
                    return k
            stack.append(i)
        return -1
"""
find the width between next_smaller and prev_smaller
b/c the mid in this range is the highest rectangle

Input: nums = [1,3,4,3,1], threshold = 6
[1,3,4,3,1]
 0,1,2,3,4
stack = 1,3
next_smaller = nums[i] = 3
mid = 4
prev_smaller = nums[stack[-1]] = 3
k = 3 - 1 + 1
min = min(next_smaller, prev_smaller)
if min > threshold / k:
    return k
"""