import collections
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        min_swap = N
        counter = collections.Counter(nums)
        if not 1 in counter:
            return 0
        window = collections.defaultdict(int)
        left = 0
        for right, num in enumerate(nums):
            window[num] += 1
            if right - left + 1 >= counter[1]:
                min_swap = min(min_swap, window[0])
                window[nums[left]] -= 1
                left += 1
        return min_swap
"""
quick sort / bubble sort?

sliding window fixed
Input: nums = [1,0,1,0,1]
counter = {1:3, 0: 2}


Input: nums = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
{1:6, 0:5 }
min_swap = 3
window = {
    1:3
    0:3
}
[1,0,1,0,1,0,0,1,1,0,1]
     l         r
"""