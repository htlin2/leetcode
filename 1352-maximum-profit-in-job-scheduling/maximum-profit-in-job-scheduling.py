class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        memo = {}
        N = len(intervals)
        def dfs(i):
            if i >= N: return 0
            if i in memo: return memo[i]
            # skip
            res = dfs(i + 1)
            # not skip
            idx = bisect.bisect_right(intervals, (intervals[i][1],))
            # if intervals[i][0] >= prev_end_time:
            #     res = max(res, dfs(i + 1, intervals[i][1]) + intervals[i][-1])
            res = max(res, dfs(idx) + intervals[i][-1])
            memo[i] = res
            return res
        return dfs(0)

"""
backtracking?
"""