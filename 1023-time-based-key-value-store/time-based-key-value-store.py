class TimeMap:

    def __init__(self):
        self.cache = collections.defaultdict(list) # key: [(time, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.cache: return ''
        time_values = self.cache[key]
        N = len(time_values)
        l, r = 0, N - 1
        while l <= r:
            m = (l + r) // 2
            # binary search weight left
            if time_values[m][0] == timestamp:
                r = m - 1
            elif time_values[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        if 0 <= l < N and time_values[l][0] == timestamp:
            return time_values[l][1]
        if 0 == l:
            return ''
        return time_values[l - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)