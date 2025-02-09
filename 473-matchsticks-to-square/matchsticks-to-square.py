class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        length = sum(nums) // 4
        if length * 4 != sum(nums): return False
        nums.sort(reverse=True)
        sides = [0] * 4
        def dfs(i):
            if i == len(nums): return True
            for j in range(4):
                if sides[j] + nums[i] <= length:
                    sides[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= nums[i]
            return False
        return dfs(0)
"""
{1: 4, 2: 2, 4: 1}

math + backtrack
how to find one side...
total / 4 = one side
pair highest with lowest to get one side?

"""