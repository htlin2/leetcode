class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        def comp(a, b):
            if a * len(b) < b * len(a):
                return -1
            return 1
        sorted_nums = sorted(nums, key=functools.cmp_to_key(comp), reverse=True)
        str_nums = ''.join(sorted_nums)
        return '0' if str_nums[0] == '0' else str_nums