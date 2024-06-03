class TimeMap:
    def __init__(self):
        # key: [(time1, value1), (t2, v2)]
        self.cache = collections.defaultdict(list)
        # Time: O(1)
        # Space: O(n)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))
        # Time: O(1)
        # Space: O(1)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache: return ''
        values = self.cache[key]
        index = bisect.bisect_left(values, (timestamp,))
        if index < len(values) and values[index][0] == timestamp:
            return values[index][-1]
        if index == 0: return ''
        return values[index - 1][-1]
        # Time: O(log n)
        # Space: O(1)
        
"""
hashmap + binary search weight left
#cache =  key: [(time1, value1), (t2, v2)]
foo: [(1, bar)]
get(foo, 0) return "" binary search weight left

"""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)