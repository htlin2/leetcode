class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        max_count, max_key = 0, 0
        for k, v in counter.items():
            if v > max_count:
                max_key = k
                max_count = v
        return max_key
        # Time: O(n)
        # Space: O(n)