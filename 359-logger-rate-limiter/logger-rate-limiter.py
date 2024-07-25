class Logger:

    def __init__(self):
        self.hashmap = {} # key: time

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hashmap and timestamp < self.hashmap[message]:
            return False
        self.hashmap[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)