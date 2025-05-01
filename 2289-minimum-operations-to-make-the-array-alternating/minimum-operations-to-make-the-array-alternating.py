class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        even_counter = collections.Counter(nums[::2])
        odd_counter = collections.Counter(nums[1::2])
        even_tuples = sorted(even_counter.items(), key=lambda x: x[-1], reverse=True)
        odd_tuples = sorted(odd_counter.items(), key=lambda x: x[-1], reverse=True)
        even_tuples.append((-1, 0))
        odd_tuples.append((-1, 0))
        if even_tuples[0][0] != odd_tuples[0][0]:
            return N - even_tuples[0][1] - odd_tuples[0][1]
        else:
            first = even_tuples[0][1] + odd_tuples[1][1]
            second = even_tuples[1][1] + odd_tuples[0][1]
            return N - max(first, second)
