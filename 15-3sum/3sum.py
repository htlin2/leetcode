class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                    l, r = l + 1, r - 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans
