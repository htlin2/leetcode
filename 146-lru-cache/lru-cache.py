class Node:
    def __init__(self, val=-1, key=-1):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, cap: int):
        head, tail = Node(), Node()
        head.next, tail.prev = tail, head
        self.cap = cap
        self.head = head
        self.tail = tail
        self.cache = {} # key: Node

    def insert(self, key, val):
        curr_node = Node(key=key, val=val)
        self.cache[key] = curr_node
        prev_node, next_node = self.head, self.head.next
        prev_node.next, next_node.prev = curr_node, curr_node
        curr_node.next, curr_node.prev = next_node, prev_node

    def remove(self, key):
        curr_node = self.cache[key]
        del self.cache[key]
        prev_node, next_node = curr_node.prev, curr_node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def remove_tail(self):
        curr_node = self.tail.prev
        self.remove(curr_node.key)

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        val = self.cache[key].val
        self.remove(key)
        self.insert(key, val)
        return self.cache[key].val

    def put(self, key: int, val: int) -> None:
        if not key in self.cache:
            self.insert(key, val)
        else:
            self.remove(key)
            self.insert(key, val)
        if len(self.cache) > self.cap:
            self.remove_tail()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)