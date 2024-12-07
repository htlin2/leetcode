class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[right]:
                return nums[left]
            if nums[left] <= nums[mid]:
                if nums[mid] >= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] <= nums[right]:
                    right = mid
                else:
                    left = mid + 1
        return nums[left]

"""
Input: nums = [4,5,6,7,0,1,2]
Output: 0


"""