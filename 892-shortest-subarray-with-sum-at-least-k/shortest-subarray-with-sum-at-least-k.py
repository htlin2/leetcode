class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefix_sums = []
        curr_sum = 0
        ans = float('inf')
        for i in range(N):
            curr_sum += nums[i]
            if curr_sum >= k:
                ans = min(ans, i + 1)
            prefix_sums.append(curr_sum)
        q = collections.deque([])
        for i in range(N):
            prefix = prefix_sums[i]
            while q and prefix - prefix_sums[q[0]] >= k:
                first = q.popleft()
                ans = min(ans, i - first)
            while q and prefix_sums[q[-1]] >= prefix_sums[i]:
                q.pop()
            q.append(i)
        return ans if ans != float('inf') else -1
"""
prefix sums + monotonic q increasing
[2,-1,2,-10,4,5
prefix_sums = -7,-3,2 k=3
              
[48,99,37,4,-31]
48,
"""