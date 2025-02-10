class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        nums.sort(reverse=True)
        visited = set()
        def bt(i, k_rem, curr_sum):
            if k_rem == 0: return True
            if curr_sum == target: 
                return bt(0, k_rem - 1, 0)
            for j in range(i, len(nums)):
                if j not in visited and curr_sum + nums[j] <= target:
                    visited.add(j)
                    if bt(j + 1, k_rem, curr_sum + nums[j]):
                        return True
                    visited.remove(j)
                    if curr_sum == 0:
                        break
            return False
        return bt(0, k, 0)