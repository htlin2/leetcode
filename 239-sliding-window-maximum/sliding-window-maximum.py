class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []
        for right in range(k):
            heapq.heappush(max_heap, (-nums[right], right))
        res.append(-max_heap[0][0])

        left = 0
        for right in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            while max_heap and max_heap[0][-1] <= left:
                heapq.heappop(max_heap)
            left += 1
            res.append(-max_heap[0][0])
        return res
