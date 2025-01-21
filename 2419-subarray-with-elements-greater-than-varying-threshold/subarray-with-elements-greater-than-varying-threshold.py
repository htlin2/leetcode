class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        stack = [] # monotonic stack increasing
        for i in range(len(nums)):
            next_smaller = nums[i]
            while stack and nums[stack[-1]] > next_smaller:
                highest_idx = stack.pop()
                k = i - stack[-1] - 1 if stack else i
                if nums[highest_idx] > threshold / k:
                    return k
            stack.append(i)
        return -1
"""
Input: nums = [1,3,4,3,1], threshold = 6
Output: 3
[ 1, 3, 4, 3, 1]
  l  r  r
k = 2
6 / 3 = 2
1.2 ~ 6

stack = [1, 3, 4, 3]


binary search
min 1 - max 8
mid == 4


"""