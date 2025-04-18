class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k: return False
        nums.sort(reverse=True)
        target = total // k
        visited = set()
        def dfs(i, curr_sum, k):
            if k == 0: return True
            if curr_sum == target: return dfs(0, 0, k - 1)
            for j in range(i, len(nums)):
                if j in visited: continue
                if curr_sum + nums[j] <= target:
                    visited.add(j)
                    if dfs(j + 1, curr_sum + nums[j], k):
                        return True
                    visited.remove(j)
                    if curr_sum == 0:
                        break
            return False
        return dfs(0, 0, k)