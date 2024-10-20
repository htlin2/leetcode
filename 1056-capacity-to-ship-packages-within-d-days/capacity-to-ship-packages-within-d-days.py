class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            total_days, curr_num = 0, 0
            for n in nums:
                if curr_num + n > mid:
                    curr_num = n
                    total_days += 1
                else:
                    curr_num += n
            if curr_num:
                total_days += 1
            if total_days == days:
                right = mid - 1
            elif total_days < days:
                # too fast, decrease load
                right = mid - 1
            else:
                left = mid + 1
        return left