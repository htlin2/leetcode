class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def split(nums):
            if len(nums) <= 1: return nums
            mid = (0 + len(nums) - 1) // 2
            A = split(nums[:mid + 1])
            B = split(nums[mid + 1:])
            return merge(A, B)
        def merge(A, B):
            i, j = 0, 0
            res = []
            while i < len(A) and j < len(B):
                if A[i] <= B[j]:
                    res.append(A[i])
                    i += 1
                else:
                    res.append(B[j])
                    j += 1
            res += A[i:] + B[j:]
            return res
        nums[:] = split(nums)