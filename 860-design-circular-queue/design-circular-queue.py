class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head, self.tail = Node(-1), Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        curr_node = Node(value)
        prev_node = self.tail.prev
        prev_node.next, curr_node.prev = curr_node, prev_node
        curr_node.next, self.tail.prev = self.tail, curr_node
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        next_node = self.head.next.next
        self.head.next, next_node.prev = next_node, self.head
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        if self.count == 0: return True
        return False

    def isFull(self) -> bool:
        if self.count == self.k: return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()