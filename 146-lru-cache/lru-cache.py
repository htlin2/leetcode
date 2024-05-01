class Node:
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, cap: int):
        head, tail = Node(), Node()
        head.next, tail.prev = tail, head
        self.cap = cap
        self.key_node = {} # key, node
        self.head = head
        self.tail = tail
    
    def add(self, prev_node, curr_node, next_node):
        prev_node.next, next_node.prev = curr_node, curr_node
        curr_node.next, curr_node.prev = next_node, prev_node
        self.key_node[curr_node.key] = curr_node
        
    def add_head(self, curr_node):
        prev_node = self.head
        next_node = self.head.next
        self.add(prev_node, curr_node, next_node)

    def pop(self, curr_node):
        prev_node, next_node = curr_node.prev, curr_node.next
        prev_node.next, next_node.prev = next_node, prev_node
        del self.key_node[curr_node.key]

    def pop_tail(self):
        self.pop(self.tail.prev)

    def get(self, key: int) -> int:
        if key not in self.key_node: return -1
        node = self.key_node[key]
        self.pop(node)
        self.add_head(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.key_node:
            old_node = self.key_node[key]
            self.pop(old_node)
        elif key not in self.key_node and len(self.key_node) == self.cap:
            self.pop_tail()
        new_node = Node(key=key, val=val)
        self.add_head(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)