class HitCounter:

    def __init__(self):
        self.q = collections.deque([])

    def hit(self, timestamp: int) -> None:
        lower_bound = timestamp - 300
        while self.q and lower_bound >= self.q[0]:
            self.q.popleft()
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        lower_bound = timestamp - 300
        while self.q and lower_bound >= self.q[0]:
            self.q.popleft()
        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)