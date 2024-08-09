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
        # while l <= r:
        #     m = (l + r) // 2
        #     if self.cache[m] <= timestamp:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # if l - 1 >= 0 and self.cache[l - 1] == timestamp:
        #     return l - 1
        # return l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# 1, 2, 3, 300