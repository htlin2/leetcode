class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even_nums = []
        odd_nums = []
        for i in range(len(nums)):
            if i % 2 == 1:
                odd_nums.append(nums[i])
            else:
                even_nums.append(nums[i])
        even_counter = collections.Counter(even_nums)
        odd_counter = collections.Counter(odd_nums)
        even_sorted = sorted(even_counter.items(), key=lambda x: x[1], reverse=True)
        odd_sorted = sorted(odd_counter.items(), key=lambda x: x[1], reverse=True)
        even_sorted.append((-1, 0))
        odd_sorted.append((-1, 0))
        if even_sorted[0][0] != odd_sorted[0][0]:
            return len(nums) - even_sorted[0][-1] - odd_sorted[0][-1]
        first = even_sorted[0][-1] + odd_sorted[1][-1]
        second = even_sorted[1][-1] + odd_sorted[0][-1]
        return len(nums) - max(first, second)