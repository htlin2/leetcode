class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            i_s, i_e = intervals[i]
            s_s, s_e = stack[-1]
            if i_s <= s_s <= i_e or s_s <= i_s <= s_e:
                stack.pop()
                stack.append([min(s_s, i_s), max(s_e, i_e)])
            else:
                stack.append([i_s, i_e])
        return stack
"""
1. sort + merge
add new interval to intervals
sort intervals by start
stack = [1, 2]
iterate through intervals:
    merge with stack if overlap
return stack
time: O(n log n)
space: O(n)


"""