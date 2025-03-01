class MyCircularQueue:

    def __init__(self, k: int):
        self.hashmap = {}
        self.head = 0
        self.curr = 0
        self.k = k - 1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.hashmap[self.curr] = value
        self.curr += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        del self.hashmap[self.head]
        self.head += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.hashmap[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.hashmap[self.curr - 1]

    def isEmpty(self) -> bool:
        if self.head == self.curr: return True
        return False

    def isFull(self) -> bool:
        if self.curr > (self.head + self.k): return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()