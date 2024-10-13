class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            total_days, curr_weight = 0, 0
            for n in nums:
                if curr_weight + n > mid:
                    total_days += 1
                    curr_weight = n
                else:
                    curr_weight += n
            if curr_weight:
                total_days += 1
            if total_days == days:
                right = mid - 1
            elif total_days < days:
                # too much weight per day, decrease weight
                right = mid - 1
            else:
                # increase package
                left = mid + 1
        return left
"""
Binary Search weight left
Input: nums = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
left, right = 10, sum(nums)

"""