class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            i_start, i_end = intervals[i]
            s_start, s_end = stack[-1]
            if s_start <= i_start <= s_end or i_start <= s_start <= i_end:
                stack.pop()
                stack.append([min(i_start, s_start), max(i_end, s_end)])
            else:
                stack.append(intervals[i])
        return stack