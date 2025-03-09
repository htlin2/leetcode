class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res, curr = 0, 1
        for i, num in enumerate(nums):
            if i + 1 < len(nums) and nums[i + 1] - num == 1:
                curr += 1
            elif i + 1 < len(nums) and nums[i + 1] - num == 0:
                continue
            else:
                curr = 1
            res = max(res, curr)
        return res