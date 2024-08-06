class TimeMap:

    def __init__(self):
        self.cache = collections.defaultdict(list) #(timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        timestamp_values = self.cache[key]
        if not timestamp_values:
            return ''
        to_find = timestamp
        idx = bisect.bisect_left(timestamp_values, [to_find, ])
        if 0 <= idx < len(timestamp_values) and timestamp_values[idx][0] == timestamp:
            return timestamp_values[idx][1]
        if idx == 0:
            return ''
        return timestamp_values[idx - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)