class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)):
            i_start, i_end = intervals[i]
            s, e = newInterval
            if i_start <= s <= i_end or s <= i_start <= e:
                newInterval = [min(i_start, s), max(i_end, e)]
            elif e < i_start:
                return ans + [newInterval] + intervals[i:]
            else:
                ans.append(intervals[i])
        return ans + [newInterval]

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