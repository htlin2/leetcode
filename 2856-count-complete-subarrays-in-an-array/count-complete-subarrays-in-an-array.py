class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq_count = len(set(nums))
        res = 0
        for i in range(len(nums)):
            visited = set()
            for j in range(i, len(nums)):
                visited.add(nums[j])
                if len(visited) == uniq_count:
                    res += 1
        return res

"""
brute force
"""