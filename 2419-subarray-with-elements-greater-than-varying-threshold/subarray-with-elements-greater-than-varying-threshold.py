class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        stack = []
        nums.append(0)  # Sentinel value to handle all elements in the stack

        for i in range(n + 1):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()
                k = i if not stack else (i - stack[-1] - 1)
                if nums[index] > threshold / k:
                    return k
            stack.append(i)

        return -1

"""
n > t / k
dfs + memo? stack?

Input: nums = [6,5,6,5,8], threshold = 7
Output: 1

[3,4,3]
"""