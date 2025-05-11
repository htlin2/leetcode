class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        prefix = [1] * N
        postfix = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                prefix[i] += prefix[i - 1]
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                postfix[i] += postfix[i + 1]
        res = []
        for i in range(N):
            res.append(max(prefix[i], postfix[i]))
        return sum(res)
"""
prefix?
stack = [1,2,]
[1,2,2,0]
[1,2,1,1]
[1,2,2,1]
[1,2,2,1] = output 6
"""