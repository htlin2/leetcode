class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while 0 <= nums[i] - 1 < N and nums[i] != nums[nums[i] - 1]:
                corr_idx = nums[i] - 1
                nums[i], nums[corr_idx] = nums[corr_idx], nums[i]
        for i in range(N):
            if nums[i] - 1 != i:
                return i + 1
        return N + 1