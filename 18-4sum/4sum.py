class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        N = len(nums)
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
        def k_sum(left, right, k, temp):
            if k < 2: return
            if k == 2:
                two_sums = two_sum(left, right, sum(temp))
                for one, two in two_sums:
                    ans.add((*temp, one, two))
            else:
                for i in range(left, right + 1):
                    k_sum(i + 1, right, k - 1, temp + [nums[i]])
        k_sum(0, N - 1, 4, [])
        return ans