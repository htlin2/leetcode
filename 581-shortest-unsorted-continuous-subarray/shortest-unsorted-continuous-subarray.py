class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = N - 1, 0
        stack = [] # monotonic increasing
        for i in range(N):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        if right > left:
            return right - left + 1
        return 0
"""
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

count + 2
stack = [2,4,8,9] monotonic increasing
[2,6,4,8,10,9,15]
            l  l         
"""