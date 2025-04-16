class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(first) and j < len(second):
            start_i, end_i = first[i]
            start_j, end_j = second[j]
            closed_start = max(start_i, start_j)
            closed_end = min(end_i, end_j)
            if closed_start <= closed_end:
                res.append([closed_start, closed_end])
            if end_i < end_j:
                i += 1
            else:
                j += 1
        return res