class MedianFinder:

    def __init__(self):
        self.max_heap = [] # left
        self.min_heap = [] # right

    def addNum(self, num: int) -> None:
        max_heap, min_heap = self.max_heap, self.min_heap
        if max_heap and -max_heap[0] >= num:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        
        while len(max_heap) < len(min_heap): #left < right
            first = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -first)
        while len(max_heap) - 1 > len(min_heap): # left - 1 > right
            first = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, first)

    def findMedian(self) -> float:
        N1, N2 = len(self.max_heap), len(self.min_heap)
        is_even = (N1 + N2) % 2 == 0
        left = -self.max_heap[0] if N1 else 0
        right = self.min_heap[0] if N2 else 0
        if is_even:
            return (left + right) / 2
        return left


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()