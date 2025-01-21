class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        N = len(heights)
        stack = [] # monotonic stack increasing
        res = 0
        for i in range(N):
            next_smaller = heights[i]
            while stack and heights[stack[-1]] > next_smaller:
                highest_idx = stack.pop()
                base = i - 1 - stack[-1] if stack else i
                area = base * heights[highest_idx]
                res = max(res, area)
            stack.append(i)
        return res

"""
monotonic stack increasing
Input: heights = [2,1,5,6,2,3]
Output: 10
[ 2, 1, 5, 6, 2, 3, 0]
  0, 1, 2, 3, 4, 5, 6
"""