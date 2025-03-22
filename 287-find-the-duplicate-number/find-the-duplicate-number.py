class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while nums[i] - 1 != i:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        for i in range(N):
            if nums[i] - 1 != i:
                return nums[i]

"""
Input: nums = [1,3,4,2,2]
Output: 2
[1,3,4,2,2]
 0,1,2,3,4
   i   j
"""