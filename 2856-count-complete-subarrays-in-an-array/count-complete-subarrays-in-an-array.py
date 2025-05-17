class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq_count = len(set(nums))
        counter = collections.defaultdict(int)
        left = 0
        res = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            while len(counter) == uniq_count:
                res += len(nums) - right
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
        return res
"""
sliding window
"""