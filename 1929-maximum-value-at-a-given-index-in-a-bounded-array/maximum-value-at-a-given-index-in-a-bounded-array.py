class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def is_valid(mid):
            # sum left side
            total = 0
            if mid <= index:
                total += (mid + 1) * mid // 2
                left_of_sequence = index - mid
                total += left_of_sequence + 1
            else:
                total += (mid + 1) * mid // 2
                left_of_sequence = mid - index - 1
                total -= left_of_sequence * (left_of_sequence + 1) // 2
            # sum right side
            if (n - index) >= mid:
                total += (mid + 1) * mid // 2
                right_of_sequence = index + mid
                total += n - right_of_sequence
            else:
                total += (mid + 1) * mid // 2
                right_of_sequence = mid - (n - index)
                total -= right_of_sequence * (right_of_sequence + 1) // 2
            return (total - mid) <= maxSum
        left, right = 0, maxSum
        res = 1
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1
        print(right)
        return right if right >= 0 else max(right, 1)
"""
index = 3
1 1 2 3 2 1 1
0 1 2 3 4 5 6

2 3 4 5
0 1 2 3 4 5


"""