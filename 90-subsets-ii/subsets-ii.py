class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def backtrack(i, temp):
            tup = tuple(temp)
            res.add(tup)
            for j in range(i, len(nums)):
                backtrack(j + 1, temp + [nums[j]])
        backtrack(0, [])
        return res

"""
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        1   2   2
       /\   /
      2  2 2
    2
how to check for duplicates?
"""