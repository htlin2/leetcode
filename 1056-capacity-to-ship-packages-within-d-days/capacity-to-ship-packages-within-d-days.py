class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        def get_count(mid):
            count = 1
            curr_total = 0
            for num in nums:
                if curr_total + num <= mid:
                    curr_total += num
                else:
                    curr_total = num
                    count += 1
            return count
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            count = get_count(mid)
            if count <= days:
                # too fast, decrease mid
                right = mid - 1
            else:
                # too slow, increase mid
                left = mid + 1
        return left
