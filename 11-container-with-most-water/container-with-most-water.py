class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        N = len(height)
        l, r = 0, N - 1
        while l < r:
            base = r - l
            min_height = min(height[l], height[r])
            res = max(res, min_height * base)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

"""
 0,1,2,3,4,5,6,7,8
[1,8,6,2,5,4,8,3,7]
 l               r
 base = r - l
 min_height = min(l, r)
 move lower r or l inside
"""