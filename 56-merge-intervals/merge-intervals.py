class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            i_s, i_e = intervals[i]
            a_s, a_e = ans[-1]
            if a_s <= i_s <= a_e or i_s <= a_s <= i_e:
                ans[-1] = [min(a_s, i_s), max(a_e, i_e)]
            else:
                ans.append([i_s, i_e])
        return ans