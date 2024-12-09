class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        window_size = sum(nums)
        window = 0
        left = 0
        max_ones = 0
        for right in range(N):
            window += nums[right]
            if right - left + 1 > window_size:
                window -= nums[left]
                left += 1
            max_ones = max(max_ones, window)
        return window_size - max_ones

"""
Input: data = [1,0,1,0,1]
Output: 1


Example 2:
Input: data = [0,0,0,1,0]
Output: 0


Input: data = [1,0,1,0,1,0,0,1,1,0,1]
               5   4   3     2 1
Output: 3
ones = 6
ans = 4

Input: data = [1,0,1,1,0,0,1,0,1,0,1]
               5   4 3     2   1
Output: 3
ones = 6
res = 2

"""