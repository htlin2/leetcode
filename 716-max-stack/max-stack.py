class MaxStack:

    def __init__(self):
        self.max_heap = [] # (-val, -id)
        self.stack = [] # (-val, -id)
        self.id = 1
        self.valid_ids = set()

    def clean_stack(self):
        while self.stack and -self.stack[-1][-1] not in self.valid_ids:
            self.stack.pop()
    
    def clean_heap(self):
        while self.max_heap and -self.max_heap[0][-1] not in self.valid_ids:
            heapq.heappop(self.max_heap)

    def push(self, x: int) -> None:
        _tuple = (-x, -self.id)
        self.valid_ids.add(self.id)
        self.stack.append(_tuple)
        heapq.heappush(self.max_heap, _tuple)
        self.id += 1
        return

    def pop(self) -> int:
        self.clean_stack()
        x, _id = self.stack.pop()
        _id *= -1
        x *= -1
        self.valid_ids.remove(_id)
        return x 

    def top(self) -> int:
        self.clean_stack()
        return -self.stack[-1][0]

    def peekMax(self) -> int:
        self.clean_heap()
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        self.clean_heap()
        x, _id = heapq.heappop(self.max_heap)
        x *= -1
        _id *= -1
        self.valid_ids.remove(_id)
        self.clean_stack()
        return x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()