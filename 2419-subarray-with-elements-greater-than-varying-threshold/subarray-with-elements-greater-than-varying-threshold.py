class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        N = len(nums)
        stack = [] # monotonic stack increasing
        for i in range(N):
            while stack and nums[stack[-1]] >= nums[i]:
                left = stack.pop()
                k = i - stack[-1] - 1 if stack else i
                if nums[left] > threshold / k:
                    return k
            stack.append(i)
        return -1
"""

"""