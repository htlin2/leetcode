class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        ans, temp = [], []
        def dfs(i, rem):
            if rem == 0:
                ans.append(temp[:])
                return
            if i >= N or rem < 0: return
            # add
            temp.append(nums[i])
            dfs(i, rem - nums[i])
            temp.pop()
            # skip
            dfs(i + 1, rem)
        dfs(0, target)
        return ans
"""
backtracking (dfs)
nums = [2,3,6,7], target = 7

            rem = 7
            /       \
i = 0    add i = 0    skip
        rem = 5       rem 7
        /   \          /  \
      add i=0 skip  i= 1    skip       
     rem = 3    rem=2
            
"""