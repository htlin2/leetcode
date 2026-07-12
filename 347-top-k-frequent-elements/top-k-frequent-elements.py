class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums) # n
        max_heap = [(-count, key) for key, count in counter.items()] # n
        heapq.heapify(max_heap) # logn
        res = []
        for i in range(k): # k
            count, key = heapq.heappop(max_heap)
            res.append(key)
        return res # k * n