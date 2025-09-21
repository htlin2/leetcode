class MaxStack:

    def __init__(self):
        self.stack = [] # (num, id)
        self.max_heap = [] # (-num, id)
        self.valid_ids = set()
        self.id = 0

    def clean(self):
        while self.stack and self.stack[-1][-1] not in self.valid_ids:
            self.stack.pop()

        while self.max_heap and -self.max_heap[0][-1] not in self.valid_ids:
            heapq.heappop(self.max_heap)

    def push(self, x: int) -> None:
        self.clean()
        self.stack.append([x, self.id])
        heapq.heappush(self.max_heap, [-x, -self.id])
        self.valid_ids.add(self.id)
        self.id += 1

    def pop(self) -> int:
        self.clean()
        num, _id = self.stack.pop()
        self.valid_ids.remove(_id)
        return num

    def top(self) -> int:
        self.clean()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self.clean()
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        self.clean()
        num, _id = heapq.heappop(self.max_heap)
        num *= -1
        self.valid_ids.remove(-_id)
        return num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()