class Solution:
    def candy(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [1] * N
        postfix = [1] * N
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                prefix[i] = prefix[i - 1] + 1
        for i in range(N - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                postfix[i] = postfix[i + 1] + 1
        res = []
        for i in range(N):
            res.append(max(prefix[i], postfix[i]))
        return sum(res)
"""
heap / greedy / monotonic stack
"""