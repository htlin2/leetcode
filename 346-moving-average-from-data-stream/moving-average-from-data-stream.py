class MovingAverage:
    def __init__(self, cap: int):
        self.q = collections.deque([])
        self.cap = cap
        self.total = 0

    def next(self, val: int) -> float:
        N = len(self.q)
        if N == self.cap:
            self.total -= self.q.popleft() 
        self.q.append(val)
        self.total += val
        return self.total / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)