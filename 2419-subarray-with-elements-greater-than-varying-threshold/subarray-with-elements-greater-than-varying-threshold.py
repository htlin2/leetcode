class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        N = len(nums)
        stack = [] # mono stack increasing
        for i in range(N):
            while stack and nums[stack[-1]] > nums[i]:
                prev_idx = stack.pop()
                prev_small = nums[prev_idx]
                k = i - stack[-1] - 1 if stack else i
                if prev_small > threshold / k:
                    return k
            stack.append(i)
        return -1
"""
stack increasing
prev small, next small
Input: nums = [1,3,4,3,1], threshold = 6
 0,1,2,3,4
[1,3,4,3,1,0]
       i
stack = [1,3,4]
prev_idx = 0
k = 2
6 / 2 = 3

"""