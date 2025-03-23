class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        if not nums or not threshold: return -1
        nums = [0] + nums + [0]
        stack = []
        for i in range(len(nums)):
            next_small = nums[i]
            while stack and nums[stack[-1]] > next_small:
                highest_idx = stack.pop()
                prev_small = nums[highest_idx]
                k = i - stack[-1] - 1 if stack else i
                if threshold / k < prev_small:
                    return k
            stack.append(i)
        return -1
"""
monotonic stack increasing
prev small, next small
Input: nums = [1,3,4,3,1], threshold = 6
Output: 3
[0, 1, 3, 4, 3, 1, 0]
 0, 1, 2, 3, 4, 5, 6
 0, 1, 2, 3, 4


Input: nums = [6,5,6,5,8], threshold = 7
Output: 1
[0, 6, 5, 6, 5, 8]
 0, 1, 2, 3, 4, 5 -> index
             i
stack = [0]
prev_small = 5
next_small = 5
base (k) = 2
target = threshold / k = 3.5

"""