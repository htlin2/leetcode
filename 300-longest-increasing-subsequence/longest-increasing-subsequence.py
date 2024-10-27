class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res or num > res[-1]:
                res.append(num)
                continue
            i = bisect.bisect_left(res, num)
            res[i] = num
        return len(res)
"""
Binary Search

"""