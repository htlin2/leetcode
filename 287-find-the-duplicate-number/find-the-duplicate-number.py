class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] - 1 != i:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                next_idx = nums[i] - 1
                nums[i], nums[next_idx] = nums[next_idx], nums[i]
        return 0
"""
two pointers - cycle detection

"""