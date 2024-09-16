class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        res = []
        def backtrack(i, temp, curr_sum):
            if curr_sum == target:
                res.append(temp)
                return
            if i == N or curr_sum > target:
                return
            # add
            backtrack(i + 1, temp + [candidates[i]], curr_sum + candidates[i])
            # skip
            while i + 1 < N and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, temp, curr_sum)
        backtrack(0, [], 0)
        return res

"""
backtracking
sort candidates
dfs(i, temp, curr_sum):
    if curr_sum == target:
        add temp to result
    add candidate
    skip candidate
time: O(2^n)
space: O(n)
"""