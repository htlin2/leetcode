class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return intervals
        intervals.sort()
        N = len(intervals)
        stack = [intervals[0]]
        for i in range(1, N):
            s, e = stack[-1]
            i_s, i_e = intervals[i]
            if s <= i_s <= e or i_s <= s <= i_e:
                stack.pop()
                merged = [min(s, i_s), max(e, i_e)]
                stack.append(merged)
            else:
                stack.append(intervals[i])
        return stack
"""
stack
sort intervals
stack = [[2,6], [8, 10]]
time: O(n log n)
space: O(n)
"""