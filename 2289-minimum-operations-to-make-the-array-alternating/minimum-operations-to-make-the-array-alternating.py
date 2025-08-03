class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd = collections.Counter(nums[1::2])
        even = collections.Counter(nums[::2])
        # num: count
        odd_sorted = sorted(odd.items(), key=lambda x: x[1], reverse=True)
        even_sorted = sorted(even.items(), key=lambda x: x[1], reverse=True)
        odd_sorted.append((-1, 0))
        even_sorted.append((-1, 0))
        N = len(nums)
        if odd_sorted[0][0] != even_sorted[0][0]:
            return N - (odd_sorted[0][-1] + even_sorted[0][-1])
        else:
            first = odd_sorted[0][-1] + even_sorted[1][-1]
            second = odd_sorted[1][-1] + even_sorted[0][-1]
            return N - max(first, second)