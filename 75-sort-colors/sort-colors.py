class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # quick sort
        # merge sort
        def merge(left, right):
            res = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            while i < len(left):
                res.append(left[i])
                i += 1
            while j < len(right):
                res.append(right[j])
                j += 1
            return res
        
        def split(nums):
            if len(nums) <= 1: return nums
            m = (len(nums) - 1) // 2
            left = split(nums[:m+1])
            right = split(nums[m+1:])
            return merge(left, right)
        sorted_nums = split(nums)
        nums[:] = sorted_nums