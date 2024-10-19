class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        stack = [] # monotonic stack increasing
        nums.append(0)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                left = stack.pop()
                k = i - stack[-1] - 1 if stack else i
                if nums[left] > threshold / k:
                    return k
            stack.append(i)
        return -1
"""
monotonic stack increasing
Input: nums = [1,3,4,3,1], threshold = 6
output: 3 -> 3,4,3
stack = [1,3,3,1]


num 1, 3, 4, 3, 1, 0
idx 0, 1, 2, 3, 4, 5

"""