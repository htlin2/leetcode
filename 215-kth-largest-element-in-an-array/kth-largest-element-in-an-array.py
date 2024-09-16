class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums
        heapq.heapify(min_heap)
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        return min_heap[0]

"""
Input: nums = [3,2,1,5,6,4], k = 2
min_heap = [1,2,3,4,5,6]
pop min_heap till len(min_heap) == k
"""