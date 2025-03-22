class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while nums[i] < N - 1 and nums[i] != nums[nums[i]]:
                correct_idx = nums[i]
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        for i, num in enumerate(nums):
            if i != num:
                return i
        return N