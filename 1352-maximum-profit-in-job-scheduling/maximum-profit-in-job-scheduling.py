class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        N = len(intervals)
        memo = {}
        def dfs(i):
            if i >= N: return 0
            if i in memo: return memo[i]
            # skip
            res = dfs(i + 1)
            # not skip
            idx = bisect.bisect_left(intervals, (intervals[i][1],))
            res = max(res, dfs(idx) + intervals[i][-1])
            memo[i] = res
            return res
        return dfs(0)

"""
backtracking + memo + Binary search
"""