class MyHashMap:

    def __init__(self):
        self.bucket = [None] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.bucket[key] = value

    def get(self, key: int) -> int:
        value = self.bucket[key]
        return -1 if value == None else value

    def remove(self, key: int) -> None:
        self.bucket[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)