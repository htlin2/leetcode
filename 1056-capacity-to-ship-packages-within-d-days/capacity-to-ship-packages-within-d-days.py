class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            total_days, curr_weight = 0, 0
            for n in nums:
                if curr_weight + n > mid:
                    curr_weight = n
                    total_days += 1
                else:
                    curr_weight += n
            if curr_weight:
                total_days += 1
            if total_days == days:
                right = mid - 1
            elif total_days < days:
                # too fast, decrease load
                right = mid - 1
            else:
                # too slow, increase load
                left = mid + 1
        return left