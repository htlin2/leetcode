class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float('inf')
        prefix_sums = []
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum >= k:
                res = min(res, i + 1)
            prefix_sums.append(curr_sum)

        q = collections.deque([])
        for i in range(len(prefix_sums)):
            while q and prefix_sums[i] - prefix_sums[q[0]] >= k:
                first = q.popleft()
                res = min(res, i - first)
            while q and prefix_sums[q[-1]] > prefix_sums[i]:
                q.pop()
            q.append(i)
        return -1 if res == float('inf') else res