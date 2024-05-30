class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
"""
binary search
 0 1 2 3 4 5 6
[0,1,2,4,5,6,7]
[4,5,6,7,0,1,2], target = 0
 l     m     r

left - Mid is sorted
1. target is in left - mid
    search left
2. target is outside of left - mid
    search right

       mid - right is sorted
3. target is in mid - right
    search right
4. target is outside of mid - right
    search mid

Time: O(log n)
Space: O(1)

brute force is go through nums with for loop
Time: O(n)
Space: O(1)
"""