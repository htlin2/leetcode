class MaxStack:
    def __init__(self):
        self.stack = [] # (val, i)
        self.max_heap = [] # (-val, -i)
        self.i = 0
        self.valid_i = set()

    def clean_stack(self):
        while self.stack and self.stack[-1][-1] not in self.valid_i:
            self.stack.pop()

    def clean_heap(self):
        while self.max_heap and -self.max_heap[0][-1] not in self.valid_i:
            heapq.heappop(self.max_heap)

    def push(self, x: int) -> None:
        self.stack.append((x, self.i))
        heapq.heappush(self.max_heap, (-x, -self.i))
        self.valid_i.add(self.i)
        self.i += 1

    def pop(self) -> int:
        self.clean_stack()
        val, i = self.stack.pop()
        self.valid_i.remove(i)
        return val

    def top(self) -> int:
        self.clean_stack()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self.clean_heap()
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        self.clean_heap()
        val, i = heapq.heappop(self.max_heap)
        val *= -1
        i *= -1
        self.valid_i.remove(i)
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()