class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            if not res or nums[i] > res[-1]:
                res.append(nums[i])
                continue
            idx = bisect.bisect_left(res, nums[i])
            res[idx] = nums[i]
        return len(res)