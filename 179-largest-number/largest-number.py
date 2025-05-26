class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        sorted_nums = sorted(nums, key=lambda x: x * 10, reverse=True)
        return ''.join(sorted_nums) if sorted_nums[0] != '0' else '0'