class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        def get_count(mid):
            count = 0
            curr_total = 0
            for num in nums:
                if curr_total + num > mid:
                    count += 1
                    curr_total = num
                    continue
                curr_total += num
            if curr_total:
                count += 1
            return count
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            count = get_count(mid)
            if count == days:
                right = mid - 1
            elif count < days:
                # too fast, decrease mid
                right = mid - 1
            else:
                # too slow, increase mid
                left = mid + 1
        return left
"""
binary search weight left
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15



Input: weights = [3,2,2,4,1,4], days = 3
Output: 6

"""