class Logger:

    def __init__(self):
        self.hashmap = {} # key: time

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if not message in self.hashmap:
            self.hashmap[message] = timestamp + 10
            return True
        time_limit = self.hashmap[message]
        if timestamp < time_limit: return False
        self.hashmap[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)