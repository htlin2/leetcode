class TimeMap:

    def __init__(self):
        self.cache = collections.defaultdict(list) #key: [(time, val)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.cache: 
            return ''
        time_values = self.cache[key]
        N = len(time_values)
        to_find = (timestamp,)
        idx = bisect.bisect_left(time_values, to_find)
        if 0 <= idx < N:
            if time_values[idx][0] == timestamp:
                return time_values[idx][1]
        if 0 == idx:
            return ''
        return time_values[idx - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)