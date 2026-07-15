class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = set()
        def two_sum(left, right, i):
            while left < right:
                triplet = (nums[left], nums[right], nums[i])
                total = nums[left] + nums[right] + nums[i]
                if total == 0 and triplet not in res:
                    res.add(triplet)
                    left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        for i in range(N - 2):
            two_sum(i + 1, N - 1, i)
        return list(res)
"""
1.brute force
3 for loops
T:O(n^3)
S:O(1)

2.

"""