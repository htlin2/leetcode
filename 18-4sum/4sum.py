class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        def two_sum(left, right, curr_sum):
            res = set()
            while left < right:
                total = nums[left] + nums[right] + curr_sum
                if total == target:
                    res.add((nums[left], nums[right]))
                if total < target:
                    left += 1
                else:
                    right -= 1
            return res
        def k_sum(i, k, temp):
            if k < 2: return
            if k == 2:
                two_sums = two_sum(i, len(nums) - 1, sum(temp))
                for one, two in two_sums:
                    ans.add((*temp, one, two))
            else:
                for j in range(i, len(nums)):
                    k_sum(j + 1, k - 1, temp + [nums[j]])
        k_sum(0, 4, [])
        return ans