class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = collections.defaultdict(int)
        for i, num in enumerate(nums):
            h[num] = i

        for i, num in enumerate(nums):
            delta = target - num
            if delta in h and h[delta] != i:
                return [i, h[delta]]