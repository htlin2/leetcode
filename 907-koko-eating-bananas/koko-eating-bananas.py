class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            total = sum([math.ceil(p / mid) for p in piles])
            if total <= h:
                # eat too fast, dec mid
                right = mid - 1
            else:
                # eat too slow, inc mid
                left = mid + 1
        return left
"""
binary search weight left
find mid (speed per hour)
calculate total hours needed
if total == h:
    eat too fast, decrease mid
elif total > h:
    eat too slow, increase mid
elif total < h:
    eat too fast, decrease mid
"""