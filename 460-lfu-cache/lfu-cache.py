class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 0
        self.prev = None
        self.next = None

class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.total_nodes = 0
        self.key_node_map = {} # key: node
        self.count_ll_map = {} # count: {head, tail}

    def insert(self, node):
        self.key_node_map[node.key] = node
        self.total_nodes += 1
        node.count += 1
        if node.count not in self.count_ll_map:
            head, tail = Node(-1, -1), Node(-1, -1)
            head.next, tail.prev = tail, head
            self.count_ll_map[node.count] = {'head': head, 'tail': tail}
        head = self.count_ll_map[node.count]['head']
        next_node = head.next
        head.next, node.prev = node, head
        node.next, next_node.prev = next_node, node
        return node

    def remove(self, node):
        self.total_nodes -= 1
        del self.key_node_map[node.key]
        prev_node, next_node = node.prev, node.next
        if prev_node.val == -1 and next_node.val == -1:
            del self.count_ll_map[node.count]
        prev_node.next, next_node.prev = next_node, prev_node
        return node

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1
        node = self.key_node_map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.val = value
            self.get(node.key)
        else:
            if self.total_nodes == self.cap:
                min_count_key = min(self.count_ll_map)
                tail_node = self.count_ll_map[min_count_key]['tail']
                LRU_node = tail_node.prev
                self.remove(LRU_node)
            node = Node(key, value)
            self.insert(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)