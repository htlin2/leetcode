class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        prefix_sums = []
        curr_sum = 0
        res = float('inf')
        # prefix sums
        for i, n in enumerate(nums):
            curr_sum += n
            if curr_sum >= k:
                res = min(res, i + 1)
            prefix_sums.append(curr_sum)
        # monotonic q
        N = len(nums)
        q = collections.deque()
        for i in range(N):
            while q and prefix_sums[i] - prefix_sums[q[0]] >= k:
                first = q.popleft()
                res = min(res, i - first)
            while q and prefix_sums[q[-1]] >= prefix_sums[i]:
                q.pop()
            q.append(i)
        return -1 if res == float('inf') else res

"""
monotonic queue increasing + prefix sums
k = 22
queue= [2, 5, 11, 18]
nums = [2, -1, -2, -3, 4, 5, 6, 7]
prefx=  2,  1, -1, -4, 0, 5, 11,18
         /
        /
\      /
 \    /
  \__/
"""