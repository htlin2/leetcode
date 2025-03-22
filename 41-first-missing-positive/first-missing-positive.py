class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while 1 <= nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1
        return N + 1