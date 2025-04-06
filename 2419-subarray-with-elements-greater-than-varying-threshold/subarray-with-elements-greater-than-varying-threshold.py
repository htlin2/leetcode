class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        stack = [] # monotonic stack increasing
        for i in range(len(nums)):
            next_smaller = nums[i]
            while stack and nums[stack[-1]] > next_smaller:
                idx = stack.pop()
                k = i - stack[-1] - 1 if stack else i
                if nums[idx] > threshold / k:
                    return k
            stack.append(i)
        return -1