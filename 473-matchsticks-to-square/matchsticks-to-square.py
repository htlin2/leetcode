class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total = sum(nums)
        length = total // 4
        if length * 4 != total: return False
        nums.sort(reverse=True)
        sides = [0] * 4
        def backtrack(i):
            if i == len(nums): return True
            for j in range(4):
                if sides[j] + nums[i] <= length:
                    sides[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= nums[i]
            return False
        return backtrack(0)