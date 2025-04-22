class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(first) and j < len(second):
            i_start, i_end = first[i]
            j_start, j_end = second[j]
            closed_start = max(i_start, j_start)
            closed_end = min(i_end, j_end)
            if closed_start <= closed_end:
                res.append([closed_start, closed_end])
            if i_end <= j_end:
                i += 1
            else:
                j += 1
        return res
"""
interval
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

first
[0,2],[5,10],[13,23],[24,25]
   i

second
[1,5],[8,12],[15,24],[25,26]
   j
max start, min end

move smaller end to next
"""