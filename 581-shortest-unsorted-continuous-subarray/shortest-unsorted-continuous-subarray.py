class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = N - 1, 0
        stack = [] # mono stack increasing
        for i in range(N):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)
        stack = [] # mono stack decreasing
        for i in range(N - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        if left < right:
            return right - left + 1
        return 0
"""
Input: nums = [2,6,4,8,10,9,15]
Output: 5
monotonic stack increasing
[2,6,4,8,10,9,15]
 2,6,
left = 1
monotonic stack decreasing
15,9,10
right = 9
"""