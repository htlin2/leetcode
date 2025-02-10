class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 4 != 0: return False
        target = total // 4
        visited = set()
        def bt(i, rem, curr_sum):
            if rem == 0: return True
            if curr_sum == target:
                return bt(0, rem - 1, 0)
            for j in range(i, len(nums)):
                if j not in visited and curr_sum + nums[j] <= target:
                    visited.add(j)
                    if bt(j + 1, rem, curr_sum + nums[j]):
                        return True
                    visited.remove(j)
                    if curr_sum == 0:
                        break
            return False
        return bt(0, 4, 0)