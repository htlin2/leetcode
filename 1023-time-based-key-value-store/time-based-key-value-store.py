class TimeMap:

    def __init__(self):
        self.cache = collections.defaultdict(list) # (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        time_values = self.cache[key]
        if not time_values: return ''
        to_find = timestamp
        idx = bisect.bisect_right(time_values, (to_find,))
        if 0 <= idx < len(time_values) and time_values[idx][0] == timestamp:
            return time_values[idx][-1]
        if idx - 1 < 0:
            return ''
        return time_values[idx - 1][-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)