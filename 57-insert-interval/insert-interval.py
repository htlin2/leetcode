class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            i_s, i_e = interval
            s, e = newInterval
            if i_s <= s <= i_e or s <= i_s <= e:
                s = min(i_s, s)
                e = max(i_e, e)
                newInterval = [s, e]
            elif e < i_s:
                res.append(newInterval)
                newInterval = interval
            else:
                res.append(interval)
        return res + [newInterval]