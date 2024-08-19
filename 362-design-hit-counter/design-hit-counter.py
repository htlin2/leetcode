class HitCounter:

    def __init__(self):
        self.cache = []

    def hit(self, timestamp: int) -> None:
        self.cache.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # bisect right
        to_find = timestamp - 300
        lower_bound = bisect.bisect_right(self.cache, to_find)
        return len(self.cache) - lower_bound



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)