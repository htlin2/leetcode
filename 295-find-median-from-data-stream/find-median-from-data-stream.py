class MedianFinder:

    def __init__(self):
        self.left = [] # max_heap
        self.right = [] # min_heap

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        if len(self.left) - len(self.right) >= 2:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) - len(self.left) >= 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        left_n, right_n = len(self.left), len(self.right)
        if (left_n + right_n) % 2 == 1:
            # odd
            return float(-self.left[0])
        else:
            # even
            return (-self.left[0] + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()