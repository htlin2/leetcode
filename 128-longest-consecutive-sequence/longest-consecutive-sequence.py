class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                curr = 0
                while num in nums_set:
                    curr += 1
                    num += 1
                res = max(res, curr)
        return res
"""
hashmap

"""