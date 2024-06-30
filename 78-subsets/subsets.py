class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(i, temp):
            nonlocal ans
            ans.append(temp[:])
            for j in range(i, len(nums)):
                temp.append(nums[j])
                dfs(j + 1, temp)
                temp.pop()
        dfs(0, [])
        return ans
"""
backtracking
[1,2,3]
        []
    [1]    [2]    [3]
[1,2] 1,3  2,3
1,2,3
"""