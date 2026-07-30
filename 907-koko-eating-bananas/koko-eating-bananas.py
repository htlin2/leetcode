class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2 # speed
            total_time = sum([math.ceil(p / mid) for p in piles])
            if total_time == h:
                right = mid
            elif total_time < h:
                # eating too fast, slow down, mid-
                right = mid
            else:
                # eating too slow, speed up, mid+
                left = mid + 1
        return left