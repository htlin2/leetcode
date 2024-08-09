class HitCounter:

    def __init__(self):
        self.q = collections.deque([]) # (timestamp, count)

    def hit(self, timestamp: int) -> None:
        min_time = timestamp - 300
        while self.q and self.q[0][0] <= min_time:
            self.q.popleft()
        if not self.q:
            self.q.append([timestamp, 1])
        elif self.q[-1][0] == timestamp:
            self.q[-1][-1] += 1
        else:
            self.q.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        min_time = timestamp - 300
        while self.q and self.q[0][0] <= min_time:
            self.q.popleft()
        res = 0
        for t, c in self.q:
            res += c
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)