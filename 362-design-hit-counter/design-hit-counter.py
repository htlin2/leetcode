class HitCounter:

    def __init__(self):
        self.cache = []

    def hit(self, timestamp: int) -> None:
        self.cache.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # bisect right (bs weight right)
        N = len(self.cache)
        to_find = timestamp - 300
        l, r = 0, N - 1
        while l <= r:
            m = (l + r) // 2
            if self.cache[m] == to_find:
                l = m + 1
            elif self.cache[m] < to_find:
                l = m + 1
            else:
                r = m - 1
        return N - l



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)