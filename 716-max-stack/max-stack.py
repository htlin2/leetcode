class MaxStack:
    def __init__(self):
        self.stack = [] # (val, idx)
        self.max_heap = [] # (-val, -idx)
        self.valid_idx = set()
        self.idx = 0

    def clean_stack(self):
        while self.stack and self.stack[-1][-1] not in self.valid_idx:
            self.stack.pop()

    def clean_max_heap(self):
        while self.max_heap and -self.max_heap[0][-1] not in self.valid_idx:
            heapq.heappop(self.max_heap)

    def push(self, x: int) -> None:
        self.stack.append((x, self.idx))
        heapq.heappush(self.max_heap, (-x, -self.idx))
        self.valid_idx.add(self.idx)
        self.idx += 1

    def pop(self) -> int:
        self.clean_stack()
        val, idx = self.stack.pop()
        self.valid_idx.remove(idx)
        return val

    def top(self) -> int:
        self.clean_stack()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self.clean_max_heap()
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        self.clean_max_heap()
        val, idx = heapq.heappop(self.max_heap)
        val *= -1
        idx *= -1
        self.valid_idx.remove(idx)
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()