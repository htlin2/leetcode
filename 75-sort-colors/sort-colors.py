class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(start, end):
            pi = nums[end]
            left = start
            for right in range(start, end):
                if nums[right] > pi:
                    continue
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            nums[left], nums[end] = nums[end], nums[left]
            return left
        def qs(start, end):
            if start <= end:
                pi = partition(start, end)
                qs(start, pi - 1)
                qs(pi + 1, end)
        qs(0, len(nums) - 1)
 
"""
merge sort
quick sort
        
"""