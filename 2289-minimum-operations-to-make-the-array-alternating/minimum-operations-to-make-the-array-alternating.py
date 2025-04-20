class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even = collections.Counter(nums[::2])
        odd = collections.Counter(nums[1::2])
        even_common = even.most_common() # sorted_count (key, count)
        odd_common = odd.most_common() # sorted_count (key, count)
        even_common.append((-1, 0))
        odd_common.append((-1, 0))
        if even_common[0][0] != odd_common[0][0]:
            return len(nums) - (even_common[0][-1] + odd_common[0][-1])
        else:
            first = even_common[0][-1] + odd_common[1][-1]
            second = even_common[1][-1] + odd_common[0][-1]
            return len(nums) - max(first, second)