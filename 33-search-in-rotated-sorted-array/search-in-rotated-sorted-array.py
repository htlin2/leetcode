class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # if left is sorted
            if nums[left] <= nums[mid]:
                # target is in sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # target is not in sorted
                else:
                    left = mid + 1
            # if right is sorted
            else:
                # target is in sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                # target is not in sorted
                else:
                    right = mid - 1
        return -1
"""
binary search
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


"""