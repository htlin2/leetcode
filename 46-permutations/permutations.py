class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, visited = [], set()
        def dfs(temp):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return
            for n in nums:
                if n in visited: continue
                visited.add(n)
                dfs(temp + [n])
                visited.remove(n)
        dfs([])
        return ans
"""
Backtracking
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    [1]     [2]     [3]
    / \     / \     / \
   [2] [3] [1] [3] [1] [2]
   [3] [2] [3] [1] [2] [1]
visited = set()
def dfs(temp = []):
    base case: if len(temp) >= len(nums):
        ans.append(temp[:])
        return
    for n in nums:
        if n in visited: continue
        visited.add(n)
        dfs(temp + n)
        visited.remove(n)


"""