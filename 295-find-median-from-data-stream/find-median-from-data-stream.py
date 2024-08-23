class MedianFinder:

    def __init__(self):
        self.left = [] # max_heap
        self.right = [] # min_heap

    def addNum(self, num: int) -> None:
        if self.left and num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        if len(self.left) - len(self.right) >= 2:
            left_val = heapq.heappop(self.left)
            heapq.heappush(self.right, -left_val)
        if len(self.right) - len(self.left) >= 2:
            right_val = heapq.heappop(self.right)
            heapq.heappush(self.left, -right_val)
        # Time: O(log n)
        # Space: O(n

    def findMedian(self) -> float:
        is_even = len(self.left) == len(self.right)
        if is_even:
            return (-self.left[0] + self.right[0]) / 2
        return float(-self.left[0]) if len(self.left) > len(self.right) else float(self.right[0])
        # Time: O(1)
        # Space: O(1)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()