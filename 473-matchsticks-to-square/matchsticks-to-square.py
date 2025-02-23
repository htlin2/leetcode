class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 4 != 0: return False
        target = total // 4
        visited = set()
        nums.sort(reverse=True)
        def bt(i, curr_sum, rem_side):
            if rem_side == 0: return True
            if curr_sum == target:
                return bt(0, 0, rem_side - 1)
            for j in range(i, len(nums)):
                if j in visited or curr_sum + nums[j] > target: continue
                visited.add(j)
                if bt(j + 1, curr_sum + nums[j], rem_side): return True
                visited.remove(j)
                # if curr_sum == 0: break
            return False
        return bt(0, 0, 4)
"""
backtracking
"""