class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack increasing
        N = len(heights)
        res = 0
        stack = [] # (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][-1] >= h:
                index, height = stack.pop()
                base = i - index
                area = base * height
                res = max(res, area)
                start = index
            res = max(res, h)
            stack.append([start, h])
        for index, height in stack:
            area = (N - index) * height
            res = max(res, area)
        return res