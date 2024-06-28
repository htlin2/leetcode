class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        rem = total // 2
        memo = {} # (rem, i): bool
        def dfs(rem, i):
            if rem == 0: return True
            if i >= len(nums) or rem < 0: return False
            if (rem, i) in memo: return memo[rem, i]
            # add or skip
            res = dfs(rem - nums[i], i + 1) or dfs(rem, i + 1)
            memo[rem, i] = res
            return res
        return dfs(rem, 0)

"""
edge case: not equal sum when odd number
backtracking to see if combination result can be added to total / 2
2 choices
dfs(rem, i)
1) add the number
2) skip the number
time: O(2^n)
space: O(n)

add cache to make it faster
memo = {} # (rem, i): bool
"""