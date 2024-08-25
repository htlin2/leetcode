class RandomizedSet:

    def __init__(self):
        self.cache = set()

    def insert(self, val: int) -> bool:
        if val in self.cache: return False
        self.cache.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache: return False
        self.cache.remove(val)
        return True

    def getRandom(self) -> int:
        to_find = list(self.cache)
        pick = random.randrange(0, len(to_find))
        return to_find[pick]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()