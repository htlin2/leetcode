class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        sorted_nums = sorted(nums)
        left, right = 0, N - 1
        while left <= right and nums[left] == sorted_nums[left]:
            left += 1
        while left <= right and nums[right] == sorted_nums[right]:
            right -= 1
        return right - left + 1
"""
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

count + 2
stack = [2,4,8,9] monotonic increasing
[2,6,4,8,10,9,15]
            l  l         
"""