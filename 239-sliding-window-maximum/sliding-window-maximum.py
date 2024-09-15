class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque([]) # monotonic q decreasing
        left = 0
        for right, n in enumerate(nums):
            while q and q[0] < left:
                q.popleft()
            while q and (nums[q[-1]] <= n):
                q.pop()
            q.append(right)
            if right < k - 1:
                continue
            res.append(nums[q[0]])
            left += 1
        return res

"""
sliding window fixed
time: O(n * k)
space: O(n)

sliding window fixed + monotonic q decreasing
time: O(n)
space: O(n)
"""