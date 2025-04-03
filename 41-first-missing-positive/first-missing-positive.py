class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while 1 <= nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1
        return N + 1

"""
Input: nums = [3,4,-1,1]
[ 3, 4,-1, 1]
  0, 1, 2, 3
  1,-1 ,3, 4
           i 
"""