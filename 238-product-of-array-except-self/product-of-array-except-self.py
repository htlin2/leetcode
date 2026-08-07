class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = []
        curr = 1
        for i in range(N):
            curr *= nums[i]
            prefix.append(curr)

        postfix = []
        curr = 1
        for i in range(N - 1, -1, -1):
            curr *= nums[i]
            postfix.append(curr)
        postfix.reverse()

        res = []
        for i in range(N):
            curr = 1
            if i + 1 < N:
                curr *= postfix[i + 1]
            if i - 1 >= 0:
                curr *= prefix[i - 1]
            res.append(curr)
        return res