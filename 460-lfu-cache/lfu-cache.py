class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.count = 1

class LFUCache:
    def __init__(self, cap: int):
        self.key_node_map = {} # key: Node
        self.count_ll_map = {} # count: {head, tail}
        self.cap = cap
        
    def insert(self, node):
        if node.count not in self.count_ll_map:
            head, tail = Node(-1, -1), Node(-1, -1)
            head.next, tail.prev = tail, head
            self.count_ll_map[node.count] = {'head': head, 'tail': tail}
        head = self.count_ll_map[node.count]['head']
        next_node = head.next
        node.next, node.prev = next_node, head
        head.next, next_node.prev = node, node
        self.key_node_map[node.key] = node
        return node

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        if prev_node.key == -1 and next_node.key == -1:
            del self.count_ll_map[node.count]
        else:
            prev_node.next, next_node.prev = next_node, prev_node
        del self.key_node_map[node.key]
        return node

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1
        node = self.key_node_map[key]
        self.remove(node)
        node.count += 1
        self.insert(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key not in self.key_node_map:
            node = Node(key, val)
            if len(self.key_node_map) == self.cap:
                min_key = min(self.count_ll_map.keys())
                LRU_node = self.count_ll_map[min_key]['tail'].prev
                self.remove(LRU_node)
            self.insert(node)
        else:
            self.get(key)
            node = self.key_node_map[key]
            node.val = val

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)