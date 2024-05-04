class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        # add first point to stack
        points.sort()
        stack = [points[0]]
        # iterate throught points[1:]:
        for p_start, p_end in points[1:]:
            # check if point overlap with stack[-1]
            is_overlap = (p_start <= stack[-1][0] <= p_end or stack[-1][0] <= p_start <= stack[-1][-1])
            if is_overlap:
                s_start, s_end = stack.pop()
                # get start = max(p1_start, stack_start)
                start = max(p_start, s_start)
                # get end = min(p1_start, stack_end)
                end = min(p_end, s_end)
                stack.append([start, end])
            else:
                stack.append([p_start, p_end])
        return len(stack)