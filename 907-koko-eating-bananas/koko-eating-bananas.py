class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, sum(piles)
        while left <= right:
            speed = (left + right) // 2
            total_hours = sum([math.ceil(p / speed) for p in piles])
            if total_hours == h:
                # decrease speed
                right = speed - 1
            elif total_hours > h:
                # increase speed
                left = speed + 1
            elif total_hours < h:
                # decrease speed
                right = speed - 1
        return left

"""
binary search shift left
speed 1, 2, 3, 4, 5, 6, 7, 8, 9
hour 10, 9, 8, 8, 8, 7, 7, 7, 7
h =         8
"""