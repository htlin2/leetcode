class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque([]) # monotonic decreasing
        left = -k + 1
        for right in range(len(nums)):
            while q and q[0] < left:
                q.popleft()
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            q.append(right)
            if left >= 0:
                res.append(nums[q[0]])
            left += 1
        return res