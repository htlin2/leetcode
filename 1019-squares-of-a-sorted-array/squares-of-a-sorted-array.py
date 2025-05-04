class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [n * n for n in nums]
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[right] >= nums[left]:
                res.append(nums[right])
                right -= 1
            else:
                res.append(nums[left])
                left += 1
        return res[::-1]