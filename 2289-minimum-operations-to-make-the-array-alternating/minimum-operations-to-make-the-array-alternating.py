class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd = collections.Counter(nums[::2])
        even = collections.Counter(nums[1::2])
        odd_sort = sorted(odd.items(), key=lambda tup: tup[-1], reverse=True)
        even_sort = sorted(even.items(), key=lambda tup: tup[-1], reverse=True)
        odd_sort.append((-1, 0))
        even_sort.append((-1, 0))
        if odd_sort[0][0] != even_sort[0][0]:
            # different
            first = odd_sort[0][-1]
            second = even_sort[0][-1]
            return len(nums) - first - second
        else:
            # same
            first = odd_sort[0][-1] + even_sort[1][-1]
            second = odd_sort[1][-1] + even_sort[0][-1]
            return len(nums) - max(first, second)