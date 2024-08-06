class TimeMap:

    def __init__(self):
        self.cache = collections.defaultdict(list) #(timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        timestamp_values = self.cache[key]
        to_find = timestamp
        l, r = 0, len(timestamp_values) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp_values[m][0] == timestamp:
                return timestamp_values[m][1]
            if timestamp_values[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        if 0 <= l - 1 < len(timestamp_values):
            return timestamp_values[l - 1][1]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)