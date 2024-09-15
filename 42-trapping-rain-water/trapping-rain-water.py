class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        prefix_list = []
        prefix = 0
        for h in height:
            prefix = max(h, prefix)
            prefix_list.append(prefix)
        postfix_list = []
        postfix = 0
        for i in range(N - 1, -1, -1):
            postfix = max(height[i], postfix)
            postfix_list.append(postfix)
        postfix_list.reverse()
        res = 0
        for i in range(N):
            border = min(postfix_list[i], prefix_list[i])
            water = max(border - height[i], 0)
            res += water
        return res
"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

        [0,1,0,2,1,0,1,3,2,1,2,1]
prefix = 0,1,1,2,2,2,2,3,3,3,3,3
postfix= 3,3,3,3,3,3,3,3,2,2,2,1
min    = 0,1,1,2,2,2,2,3,2,2,2,1  min(pre, post)
water  = 0,0,1,0,1,2,1,0,0,1,0,0  max(height - min, 0)
Time: O(n)
Space: O(n)
"""