class MaxStack:
    def __init__(self):
        self.stack = sortedcontainers.SortedList() # (i, val)
        self.values = sortedcontainers.SortedList() # (val, i)
        self.i = 0

    def push(self, x: int) -> None:
        self.stack.add((self.i, x))
        self.values.add((x, self.i))
        self.i += 1

    def pop(self) -> int:
        i, val = self.stack.pop()
        self.values.remove((val, i))
        return val

    def top(self) -> int:
        return self.stack[-1][-1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        val, i = self.values.pop()
        self.stack.remove((i, val))
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()