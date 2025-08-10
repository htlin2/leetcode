class Solution:
    def candy(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [1] * N
        postfix = [1] * N
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                prefix[i] += prefix[i - 1]
        for i in range(N - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                postfix[i] += postfix[i + 1]
        res = 0
        for i in range(N):
            res += max(prefix[i], postfix[i])
        return res