class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        N = len(nums)
        res = set()
        for i in range(N - 2):
            left, right = i + 1, N - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.add((nums[i], nums[left], nums[right]))
                if total <= 0:
                    # too small, incrase total
                    left += 1
                else:
                    right -= 1
        return list(res)