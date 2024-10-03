class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            total_days, curr_weight = 1, 0
            for w in weights:
                if curr_weight + w <= mid:
                    curr_weight += w
                else:
                    total_days += 1
                    curr_weight = w
            if total_days <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left
"""
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
binary search
low: 1, high: 55
mid = 10
total_days = 3
cal_days: 
    1,2,3,4,5,6,7,8,9,10
    1       2 3 4 5 6 7
"""