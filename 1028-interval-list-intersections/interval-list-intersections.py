class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(first) and j < len(second):
            i_start, i_end = first[i]
            j_start, j_end = second[j]
            start = max(i_start, j_start)
            end = min(i_end, j_end)
            if start <= end:
                res.append([start, end])
            if i_end <= j_end:
                i += 1
            else:
                j += 1
        return res
"""
max start_1, start_2
min end_1, end_2
moved to next based on the lower end value
"""