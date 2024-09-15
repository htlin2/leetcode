class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        left, right = 0, N - 1
        res = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(area, res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
 0,1,2,3,4,5,6,7,8
[1,8,6,2,5,4,8,3,7]
   l             r

 max_area = 9
 (8 - 1) = 7
 7 * min(8, 7) = 49
"""