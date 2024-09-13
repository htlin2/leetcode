class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        head, tail = Node(), Node()
        head.next, tail.prev = tail, head
        self.head = head
        self.tail = tail
        self.cache = {} # key: node

    def remove(self, node):
        key = node.key
        if not key in self.cache:
            return
        old_node = self.cache[key]
        del self.cache[key]
        prev_node, next_node = old_node.prev, old_node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def insert(self, prev_node, curr_node, next_node):
        curr_node.prev, curr_node.next = prev_node, next_node
        prev_node.next, next_node.prev = curr_node, curr_node
        self.cache[curr_node.key] = curr_node

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        # remove old_node
        old_node = self.cache[key]
        self.remove(old_node)
        # insert new_node
        new_node = Node(key, old_node.val)
        self.insert(self.head, new_node, self.head.next)
        return new_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        if self.cap == len(self.cache):
            self.remove(self.tail.prev)
        new_node = Node(key, value)
        self.insert(self.head, new_node, self.head.next)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)