class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        max_i = 0
        for i, num in enumerate(nums):
            if i > max_i:
                return False
            max_i = max(max_i, i + num)
            if max_i >= N - 1:
                return True
        return False
"""
nums = 
   [2,3,1,1,4]
cur i i i i
max 2 5 5 5
"""