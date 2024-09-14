class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        window = collections.defaultdict(int)
        left, max_f = 0, 0
        for right in range(N):
            window[nums[right]] += 1
            max_f = max(max_f, window[nums[right]])
            while (right - left + 1) - max_f > k:
                window[nums[left]] -= 1
                max_f = max(max_f, window[nums[left]])
                left += 1
        return max_f

"""
Input: nums = [1,3,2,3,1,3], k = 3
sliding window variable
window= 1:1, 3:3, 2:1, 4: 1
max_f = 3
delta = (r - l + 1) - max_f = 4 is < k? no
nums = [ 1, 3, 2, 3, 1, 3, 4]
            l              r
"""