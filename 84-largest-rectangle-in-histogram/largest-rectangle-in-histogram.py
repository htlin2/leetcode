class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack increasing
        N = len(heights)
        res = 0
        stack = [] # (index, height)
        # iterate throught heights
        for i, h in enumerate(heights):
            # while stack and top of stack is heigher than current height:
            L = i
            while stack and stack[-1][-1] >= h:
                index, height = stack.pop()
                area = height * (i - index)
                res = max(res, area)
                L = index
            res = max(res, h)
            stack.append([L, h])
        # iterate through stack and get height
        for i, h in stack:
            area = (N - i) * h
            res = max(res, area)
        return res