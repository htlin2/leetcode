class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            min_num = min(nums[i], nums[i + 1])
            res += min_num
        return res
