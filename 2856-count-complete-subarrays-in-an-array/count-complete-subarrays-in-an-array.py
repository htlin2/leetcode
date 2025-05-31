class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        res = 0
        window = collections.defaultdict(int)
        left = 0
        for right in range(len(nums)):
            window[nums[right]] += 1
            while len(window) == len(uniq_nums):
                res += len(nums) - right
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
        return res