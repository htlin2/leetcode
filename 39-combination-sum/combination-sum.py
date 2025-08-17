class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # memo = collections.defaultdict(int) # (i, rem): temp
        def backtrack(i, temp, rem):
            if rem == 0:
                res.append(temp.copy())
                return
            if rem < 0 or i >= len(nums): return
            # add
            backtrack(i, [*temp, nums[i]], rem - nums[i])
            # skip
            backtrack(i + 1, temp, rem)
        backtrack(0, [], target)
        return res
"""
backtracking
"""