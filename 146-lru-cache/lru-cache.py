class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, cap: int):
        # hashmap + LL
        # handle cap
        # key_node_map = {key: Node}
        # MRU (head) -> LRU (tail)
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = cap
        self.key_node_map = collections.defaultdict(Node)

    def _insert_node(self, key, value):
        node = Node(key, value)
        self.key_node_map[key] = node
        prev_node = self.head.next
        self.head.next, node.prev = node, self.head
        prev_node.prev, node.next = node, prev_node
        return node

    def _remove_node(self, key):
        curr_node = self.key_node_map[key]
        next_node, prev_node = curr_node.next, curr_node.prev
        next_node.prev, prev_node.next = prev_node, next_node
        del self.key_node_map[key]
        return curr_node

    def get(self, key: int) -> int:
        # return value associated to the key
        # return -1 if key not exist
        if key not in self.key_node_map: return -1
        curr_node = self._remove_node(key)
        self._insert_node(curr_node.key, curr_node.value)
        return curr_node.value
        

    def put(self, key: int, value: int) -> None:
        # upsert value to the key
        # if count of keys > cap, evict LRU key
        if key in self.key_node_map:
            self.get(key)
            self.key_node_map[key].value = value
        else:
            if self.cap == len(self.key_node_map):
                # evict LRU
                LRU = self.tail.prev
                self._remove_node(LRU.key)
            self._insert_node(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)