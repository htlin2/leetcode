class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # helper func to cal total hours
        def helper(piles, speed):
            res = 0
            for p in piles:
                res += math.ceil(p / speed)
            return res
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            hrs = helper(piles, mid)
            if hrs <= h:
                # decrease speed, eating too fast
                right = mid - 1
            else:
                # increase speed, eating too slow
                left = mid + 1
        return left
"""
In: 
out(speed) = 4
[3,6,7,11], h = 8
[1,2,2,3] = 8
binary search weighted left left = 1, right = 11
mid = (1 + 11) / 2 = 6
[1,1,2,2] = 6
eating too fast, decrease speed, right = m - 1
"""