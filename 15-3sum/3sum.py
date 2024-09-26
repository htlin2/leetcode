class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = set() # (n_i, n_j, n_k)
        def two_sum(n_i, left, right):
            while left < right:
                three_sum = n_i + nums[left] + nums[right]
                if three_sum == 0:
                    res.add((n_i, nums[left], nums[right]))
                if three_sum <= 0:
                    left += 1
                else:
                    right -= 1
            return 

        for i in range(0, N - 2):
            n_i = nums[i]
            two_sum(n_i, i + 1, N - 1)
        return list(res)