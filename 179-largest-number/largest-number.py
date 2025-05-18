class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        sorted_nums = sorted(str_nums, key=functools.cmp_to_key(compare))
        return str(int(''.join(sorted_nums)))