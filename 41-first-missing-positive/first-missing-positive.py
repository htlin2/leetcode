class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] - 1 != i and 0 < nums[i] < len(nums):
                next_idx = nums[i] - 1
                if nums[i] == nums[next_idx]:
                    break
                nums[i], nums[next_idx] = nums[next_idx], nums[i]
        for i in range(len(nums)):
            if nums[i] - 1 == i:
                continue
            else:
                return i + 1
        return len(nums) + 1