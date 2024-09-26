class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = []
        def two_sum(n_i, left, right):
            while left < right:
                three_sum = n_i + nums[left] + nums[right]
                if three_sum == 0:
                    res.append((n_i, nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
            return 

        for i in range(0, N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            n_i = nums[i]
            two_sum(n_i, i + 1, N - 1)
        return res