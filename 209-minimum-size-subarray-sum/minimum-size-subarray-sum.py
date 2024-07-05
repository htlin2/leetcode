class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window variable
        N = len(nums)
        res = float('inf')
        window_sum = 0
        l = 0
        for r in range(N):
            window_sum += nums[r]
            while l < N and window_sum >= target:
                res = min(res, r - l + 1)
                window_sum -= nums[l]
                l += 1
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
time: O(n * log n)
space: O(n)
"""