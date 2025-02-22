class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k: return False
        nums.sort(reverse=True)
        target = total // k
        visited = set() # index
        def dfs(i, curr_sum, k_rem):
            if k_rem == 0: return True
            if curr_sum == target: return dfs(0, 0, k_rem - 1)
            for j in range(i, len(nums)):
                if j in visited or curr_sum + nums[j] > target: continue
                visited.add(j)
                if dfs(j + 1, curr_sum + nums[j], k_rem):
                    return True
                visited.remove(j)
                if curr_sum == 0:
                    break
            return False
        return dfs(0, 0, k)

"""
backtracking
total / k to get equal sum

"""