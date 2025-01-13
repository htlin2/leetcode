class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] > nums[right]:
                nums[right - 1] += nums[right]
                right -= 1
                res += 1
            else:
                nums[left + 1] += nums[left]
                left += 1
                res += 1
        return res