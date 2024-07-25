class MedianFinder:
    def __init__(self):
        self.min_heap = [] # right
        self.max_heap = [] # left

    def addNum(self, num: int) -> None:
        min_heap, max_heap = self.min_heap, self.max_heap
        if min_heap and num < min_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(min_heap) - len(max_heap) >= 2:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) - len(min_heap) >= 2:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

    def findMedian(self) -> float:
        min_heap, max_heap = self.min_heap, self.max_heap
        if len(min_heap) > len(max_heap):
            return min_heap[0] * 1.0
        if len(max_heap) > len(min_heap):
            return max_heap[0] * -1.0
        return (min_heap[0] - max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()