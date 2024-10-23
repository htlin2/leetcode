class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}
        def dfs(i):
            if i >= N: return 0
            if i in memo: return memo[i]
            res = 1
            for j in range(i + 1, N):
                if nums[j] > nums[i]:
                    res = max(res, dfs(j) + 1)
            memo[i] = res
            return res
        ans = 0
        for i in range(N):
            ans = max(ans, dfs(i))
        return ans

"""
dfs(i, prev)
    include -> have to be bigger than previous
    not include

Input: nums = [0,1,0,3,2,3]
Output: 4
0 1 0
time: O(n)
space: O(n)
"""