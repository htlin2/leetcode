class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= ans[-1][0] <= e or ans[-1][0] <= s <= ans[-1][-1]:
                ans[-1][0] = min(s, ans[-1][0])
                ans[-1][-1] = max(e, ans[-1][-1])
            else:
                ans.append([s, e])
        return ans