class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        max_increase = 0
        for t in counter:
            if t == k: continue
            curr_sum = max_sum = 0
            for num in nums:
                if num == t:
                    curr_sum += 1
                elif num == k:
                    curr_sum -= 1
                curr_sum = max(curr_sum, 0)
                max_sum = max(max_sum, curr_sum)
            max_increase = max(max_increase, max_sum)
        return counter[k] + max_increase
"""
Input:
nums = [3, 2, 3, 7, 3, 2]
k = 2
Output: 4

t == 3
[3, 2, 3, 7, 3, 2]
[1, 0, 1, 1, 2, 1] = curr_sum
"""