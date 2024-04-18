class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in h:
                return [h[delta], i]
            h[nums[i]] = i