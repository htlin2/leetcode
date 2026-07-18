class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            speed = sum([math.ceil(p / mid) for p in piles])
            if speed > h:
                # eating too slow, speed up, increase mid
                left = mid + 1
            elif speed < h:
                # eating too fast, slow down, decrease mid
                right = mid - 1
            else:
                # same as h, slow down
                right = mid - 1
        return left
"""
binary search weight left
"""