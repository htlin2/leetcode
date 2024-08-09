class HitCounter:

    def __init__(self):
        self.cache = []

    def hit(self, timestamp: int) -> None:
        self.cache.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        N = len(self.cache)
        to_find = timestamp - 300
        idx = bisect.bisect_right(self.cache, to_find)
        return N - idx


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# 1, 2, 3, 300, 301