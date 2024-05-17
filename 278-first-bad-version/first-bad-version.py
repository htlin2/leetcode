# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
"""
1 brute force
for loop from 1 ~ n
call isBadVersion
Time: O(n)
Space: O(1)

2 binary search weighted left
left = 1, right = n
while loop left <= right:
    mid
    is_bad = isBadVersion(mid)
    if is_bad == True:
        right = mid - 1
    else:
        left = mid + 1
return left
Time: O(log n)
space: O(1)
"""