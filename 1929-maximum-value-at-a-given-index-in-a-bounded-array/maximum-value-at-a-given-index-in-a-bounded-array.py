class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        res = 1
        left, right = 0, maxSum
        
        def sequence(mid):
            total = 0
            
            # Can fit sequence on left side
            if index + 1 > mid:
                total += (mid) * (mid + 1) // 2
                left_of_sequence = index - mid
                total += left_of_sequence + 1
            # Can't fit sequence on left side
            else:
                total += (mid) * (mid + 1) // 2
                left_of_sequence = mid - (index + 1)
                total -= (left_of_sequence) * (left_of_sequence + 1) // 2
            
            end = n - 1
            # Can fit sequence on right side
            if (end - index + 1) >= mid:
                total += (mid) * (mid + 1) // 2
                right_of_sequence = index + mid
                total += end - right_of_sequence + 1
            # Can't fit sequence on right side
            else:
                total += (mid) * (mid + 1) // 2
                right_of_sequence = mid - (end + 1 - index)
                total -= (right_of_sequence) * (right_of_sequence + 1) // 2
            
            total -= mid
            return total
        
        while left <= right:
            mid = (right + left) // 2
            if sequence(mid) <= maxSum:
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1
        
        return res
