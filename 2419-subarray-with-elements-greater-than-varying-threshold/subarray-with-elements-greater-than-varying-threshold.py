class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        stack = [] # monotonic increasing
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                prev_small = nums[stack.pop()]
                k = i - stack[-1] - 1 if stack else i
                if prev_small > threshold / k:
                    return k
            stack.append(i)
        return -1