class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 0
        self.next = None
        self.prev = None

class LL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # self.key_node_map = {} # key: Node
    
    def insert(self, curr_node):
        prev_node = self.head
        next_node = self.head.next
        curr_node.next, curr_node.prev = next_node, prev_node
        prev_node.next, next_node.prev = curr_node, curr_node
        # self.key_node_map[curr_node.key] = node
        return curr_node
    
    def remove(self, curr_node):
        # del self.key_node_map[curr_node.key]
        prev_node = curr_node.prev
        next_node = curr_node.next
        prev_node.next, next_node.prev = next_node, prev_node
        return curr_node

class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.count_ll_map = {} # count: LL
        self.key_node_map = {} # key: Node

    def insert(self, node):
        node.count += 1
        if node.count in self.count_ll_map:
            ll = self.count_ll_map[node.count]
        else:
            ll = LL()
            self.count_ll_map[node.count] = ll
        ll.insert(node)
        self.key_node_map[node.key] = node
        return node
    
    def remove(self, node):
        del self.key_node_map[node.key]
        ll = self.count_ll_map[node.count]
        ll.remove(node)
        if ll.head.next.val == -1:
            del self.count_ll_map[node.count]
        return node

    def get(self, key: int) -> int:
        if key not in self.key_node_map: return -1
        node = self.key_node_map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_node_map:
            self.key_node_map[key].val = value
            self.get(key)
        else:
            node = Node(key, value)
            if self.cap == len(self.key_node_map):
                # handle LFU
                min_count = min(self.count_ll_map)
                ll = self.count_ll_map[min_count]
                LFU_node = ll.tail.prev
                self.remove(LFU_node)
            self.insert(node)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)