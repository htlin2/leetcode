class MedianFinder:

    def __init__(self):
        self.left = [] # max_heap
        self.right = [] # min_heap

    def addNum(self, num: int) -> None:
        if self.right and self.right[0] < num:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        # balance
        if len(self.right) - len(self.left) > 1:
            n = heapq.heappop(self.right)
            heapq.heappush(self.left, -n)
        elif len(self.left) - len(self.right) > 1:
            n = heapq.heappop(self.left)
            heapq.heappush(self.right, -n)

    def findMedian(self) -> float:
        N = len(self.left) + len(self.right)
        if N % 2 == 0:
            # even
            total = self.right[0] - self.left[0]
            return float(total / 2)
        # odd
        if len(self.right) - len(self.left) > 0:
            return float(self.right[0])
        return float(-self.left[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
1, 2, 3, 4, 5, 6
left = max_heap = [-1]
righ = min_heap = [2,3]



# findMedian
even
min_heap[0] + max_heap[0] / 2
odd
longest left or right
return first element
"""