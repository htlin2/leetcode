class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            total_hours = sum([math.ceil(p / mid) for p in piles])
            if total_hours == h:
                # can we slow down more?
                right = mid - 1
            elif total_hours < h:
                # eating too fast, slow down
                right = mid - 1
            else:
                # eating too slow, speed up
                left = mid + 1
        return left


"""
Input: piles = [3,6,7,11], h = 8
Output: 4

[ 3, 6, 7,11]
left = 3
right = 11
mid = (3 + 11) // 2 = 7
[1, 1, 1, 2] => 5 hours => 5 hours < 8, eating too fast need slow down

left = 3
right = 7
mid = (3 + 7) // 2 = 5
[ 1, 2, 2, 3] => 8 hours => 8 == 8, meet h, but can we slow down more?
binary search weight left

left = 3
right = 5
mid = (3 + 5) // 2 = 4
[ 1, 2, 2, 3] => 8 hours => 8 == 8, meet h, but can we slow down more?
binary search weight left

left = 3
right = 4
mid = (3 + 4) // 2 = 3
[1, 2, 3, 4] => 10 hrs > h, eating too slow need to speed up

"""