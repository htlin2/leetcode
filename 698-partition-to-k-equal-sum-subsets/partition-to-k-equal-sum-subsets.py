class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        total = sum(nums)
        target = total // k
        if target * k != total:
            return False
        nums.sort(reverse=True)
        visited = set()
        def dfs(i, curr_sum, rem_k):
            if rem_k == 0:
                return True
            if curr_sum == target:
                return dfs(0, 0, rem_k - 1)
            for j in range(i, N):
                if j in visited: continue
                if curr_sum + nums[j] <= target:
                    visited.add(j)
                    if dfs(j + 1, curr_sum + nums[j], rem_k):
                        return True
                    visited.remove(j)
                if curr_sum == 0:
                    break
            return False
        return dfs(0, 0, k)
"""
backtracking
"""