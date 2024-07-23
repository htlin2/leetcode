class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[l] <= nums[m]:
                # left sorted
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # right sorted
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
"""
binary search
find left or right side is sorted
    if target in sorted side:
        r = m - 1
    else:
        l = m + 1
    if target in not sorted side:
        
"""