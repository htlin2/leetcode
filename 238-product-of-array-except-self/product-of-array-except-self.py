class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        curr = 1
        for i in range(N):
            curr *= nums[i]
            res.append(curr)

        curr = 1
        for i in range(N - 1, -1, -1):
            prefix, postfix = 1, 1
            if i - 1 >= 0:
                prefix = res[i - 1]
            if i + 1 < N:
                postfix = curr
            res[i] = prefix * postfix
            curr *= nums[i]
        return res