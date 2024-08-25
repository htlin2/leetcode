class Node:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, cap: int):
        self.cap = cap
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {} # key: Node

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        # remove node from LL
        self.remove_node_from_ll(node)
        # add node to head
        self.add_node_to_head(node)
        return node.val

    def remove_node_from_ll(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        del self.cache[node.key]

    def add_node_to_head(self, node):
        prev_first_node = self.head.next
        self.head.next, prev_first_node.prev = node, node
        node.next, node.prev = prev_first_node, self.head
        self.cache[node.key] = node

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            curr_node = self.cache[key]
            curr_node.val = val
            self.remove_node_from_ll(curr_node)
        else:
            curr_node = Node(key=key, val=val)
            self.cache[key] = curr_node
        self.add_node_to_head(curr_node)
        if len(self.cache) > self.cap:
            # delete LRU_node
            lru_node = self.tail.prev
            self.remove_node_from_ll(lru_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
put 2,1 -> {2}
put 1,1 -> {1, 2}
put 2,3 -> {2, 1}
put 4,1 -> {4, 2}
get 1
get 2
"""