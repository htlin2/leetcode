class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # prefix sum + binary search
        N = len(nums)
        res = float('inf')
        prefix_sums = []
        prefix = 0
        for i, n in enumerate(nums):
            prefix += n
            if prefix >= target:
                res = min(res, i + 1)
            prefix_sums.append(prefix)
        for l, n in enumerate(prefix_sums):
            to_find = n + target
            r = bisect.bisect_left(prefix_sums, to_find)
            if r >= N: continue
            res = min(res, r - l)
        return res if res != float('inf') else 0
"""
1 brute force
two for loops
time: O(n^2)
space: O(1)

2 sliding window variable
for loop with right pointer
    when sum is greater than target
    shrink window with left pointer
time: O(n)
space: O(1)

3 prefix sum + binary search
target = 7, nums = 
         [2,3,1,2, 4, 3]
prefix = [2,5,6,8,12,15]
         [2,5,6,3, 4, 5]
time: O(n * log n)
space: O(n)
"""