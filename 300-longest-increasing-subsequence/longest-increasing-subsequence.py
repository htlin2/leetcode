class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res or res[-1] < num:
                res.append(num)
                continue
            idx = bisect.bisect_left(res, num)
            res[idx] = num
        return len(res)